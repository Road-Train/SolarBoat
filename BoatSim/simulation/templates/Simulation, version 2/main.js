import './style.css';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { Water } from 'three/examples/jsm/objects/Water.js';
import { Sky } from 'three/examples/jsm/objects/Sky.js';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js';

let orbitCam, detectorCam, scene, renderer;
let orbitControls, water, sun;
let useMainCamera = true;
const loader = new OBJLoader();
const buoys = [];
const renderTarget = new THREE.WebGLRenderTarget(window.innerWidth, window.innerHeight);


class Boat
{
	constructor(startPosition)
	{
		this.velocity = 0;
		this.rotationSpeed = 0;
		this.targetVel = 0;
		this.targetRot = 0;
		this.acceleration = 0.02;

		loader.load("/assets/boat/sail.obj", (obj) => 
		{
			obj.traverse(function (child) 
			{
				if (child instanceof THREE.Mesh) 
				{
					child.material.side = THREE.DoubleSide;
				}
			});

			obj.scale.set(3, 3, 3);
			obj.position.copy(startPosition);
			obj.rotation.y = 1.5;
			scene.add(obj);
			this.boat = obj;
		});
	}

	setSpeed(targetVel, targetRot) 
	{
		this.targetVel = targetVel;
		this.targetRot = targetRot;
	}

	updateSpeed()
	{
		this.velocity += (this.targetVel - this.velocity) * this.acceleration;
		this.rotationSpeed += (this.targetRot - this.rotationSpeed) * this.acceleration;
	}

	update()
	{
		if (this.boat)
		{
			this.avoidBuoys();
			this.updateSpeed();
			this.boat.rotation.y += this.rotationSpeed;
			this.boat.translateZ(this.velocity);
		}
	}

	avoidBuoys()
	{
		if (!this.boat) return;

		buoys.forEach(buoy => 
		{
			const distance = this.boat.position.distanceTo(buoy.position);
			if (distance < 15)
			{
				const angleToBuoy = Math.atan2(
					buoy.position.z - this.boat.position.z,
					buoy.position.x - this.boat.position.x
				);

				const avoidAngle = angleToBuoy + Math.PI / 2;

				this.boat.rotation.y = avoidAngle;
			}
		});
	}
	getPosition()
	{
		return this.boat ? this.boat.position : new THREE.Vector3();
	}

	getRotation()
	{
		return this.boat ? this.boat.rotation : new THREE.Euler();
	}
}

// Initialize two boats with different starting positions
const manualBoat = new Boat(new THREE.Vector3(5, -18, 50));  // Keyboard-controlled boat
const autonomousBoat = new Boat(new THREE.Vector3(10, -18, 55)); // Autonomous boat

function init()
{
	renderer = new THREE.WebGLRenderer();
	renderer.setPixelRatio(window.devicePixelRatio);
	renderer.setSize(window.innerWidth, window.innerHeight);
	renderer.toneMapping = THREE.ACESFilmicToneMapping;
	document.body.appendChild(renderer.domElement);

	scene = new THREE.Scene();

	orbitCam = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 1, 20000);
	orbitCam.position.set(30, 30, 100);
	// Initialize detectorCam
	detectorCam = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 1, 20000);
	const boatPosition = manualBoat.getPosition();
	const boatRotation = manualBoat.getRotation();
	detectorCam.position.set(
		boatPosition.x - Math.sin(boatRotation.y) * 60,  // Adjust the distance
		boatPosition.y + 25,  // Adjust the height
		boatPosition.z - Math.cos(boatRotation.y) * 60   // Adjust the distance
	);
	detectorCam.lookAt(boatPosition);
	scene.add(orbitCam);
	scene.add(detectorCam);
	sun = new THREE.Vector3();

	const waterGeometry = new THREE.PlaneGeometry(10000, 10000);
	water = new Water(
		waterGeometry,
		{
			textureWidth: 512,
			textureHeight: 512,
			waterNormals: new THREE.TextureLoader().load('assets/waternormals.jpg', function (texture)
			{
				texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
			}),
			sunDirection: new THREE.Vector3(),
			sunColor: 0xffffff,
			waterColor: 0x001e0f,
			distortionScale: 3.7,
			fog: scene.fog !== undefined
		}
	);
	water.rotation.x = -Math.PI / 2;
	scene.add(water);

	const sky = new Sky();
	sky.scale.setScalar(10000);
	scene.add(sky);

	const skyUniforms = sky.material.uniforms;
	skyUniforms['turbidity'].value = 10;
	skyUniforms['rayleigh'].value = 2;
	skyUniforms['mieCoefficient'].value = 0.005;
	skyUniforms['mieDirectionalG'].value = 0.8;

	const pmremGenerator = new THREE.PMREMGenerator(renderer);

	function updateSun()
	{
		const phi = THREE.MathUtils.degToRad(90 - 2);
		const theta = THREE.MathUtils.degToRad(180);

		sun.setFromSphericalCoords(1, phi, theta);

		sky.material.uniforms['sunPosition'].value.copy(sun);
		water.material.uniforms['sunDirection'].value.copy(sun).normalize();

		scene.environment = pmremGenerator.fromScene(sky).texture;
	}

	updateSun();

	orbitControls = new OrbitControls(orbitCam, renderer.domElement);
	orbitControls.maxPolarAngle = Math.PI * 0.495;
	orbitControls.target.set(0, 10, 0);
	orbitControls.minDistance = 40.0;
	orbitControls.maxDistance = 200.0;
	orbitControls.update();
	window.addEventListener('resize', onWindowResize);
	window.addEventListener('keydown', onKeyDown);
	window.addEventListener('keyup', onKeyUp);

	// Load and add the first buoy to the scene
	loader.load('/assets/boat/Low_Poly_Buoy.obj', (obj) =>
	{
		obj.traverse(function (child)
		{
			if (child instanceof THREE.Mesh)
			{
				child.material.side = THREE.DoubleSide;
			}
		});

		obj.scale.set(5, 5, 5);
		obj.position.set(700, -5, 250); // Adjust the position as needed
		scene.add(obj);
		buoys.push(obj);
	});

	// Load and add the second buoy to the scene
	loader.load('/assets/boat/Low_Poly_Buoy.obj', (obj) =>
	{
		obj.traverse(function (child)
		{
			if (child instanceof THREE.Mesh)
			{
				child.material.side = THREE.DoubleSide;
			}
		});

		obj.scale.set(5, 5, 5);
		obj.position.set(-400, -5, -100); // Adjust the position as needed
		scene.add(obj);
		buoys.push(obj);
	});

	// Load and add the third buoy to the scene
	loader.load('/assets/boat/Low_Poly_Buoy.obj', (obj) =>
	{
		obj.traverse(function (child)
		{
			if (child instanceof THREE.Mesh)
			{
				child.material.side = THREE.DoubleSide;
			}
		});

		obj.scale.set(5, 5, 5);
		obj.position.set(50, -5, -20); // Adjust the position as needed
		scene.add(obj);
		buoys.push(obj);
	});
}

function onWindowResize()
{
	orbitCam.aspect = window.innerWidth / window.innerHeight;
	orbitCam.updateProjectionMatrix();
	renderer.setSize(window.innerWidth, window.innerHeight);
}

let keys = {};

function onKeyDown(event)
{
	keys[event.key] = true;

	if (keys['ArrowUp'])
	{
		manualBoat.setSpeed(-1.0, manualBoat.targetRot); // Move forward
	}
	if (keys['ArrowDown'])
	{
		manualBoat.setSpeed(1.0, manualBoat.targetRot); // Move backward
	}
	if (keys['ArrowLeft'])
	{
		manualBoat.setSpeed(manualBoat.targetVel, 0.02); // Turn left
	}
	if (keys['ArrowRight'])
	{
		manualBoat.setSpeed(manualBoat.targetVel, -0.02); // Turn right
	}
	if (keys['v'])
	{
		console.log("V");
		switchCamera();
	}
}

function onKeyUp(event)
{
	keys[event.key] = false;

	if (!keys['ArrowUp'] && !keys['ArrowDown'])
	{
		manualBoat.setSpeed(0, manualBoat.targetRot); // Stop moving
	}
	if (!keys['ArrowLeft'] && !keys['ArrowRight'])
	{
		manualBoat.setSpeed(manualBoat.targetVel, 0); // Stop rotating
	}
}
function switchCamera()
{
	useMainCamera = !useMainCamera;
	const boatPosition = manualBoat.getPosition();
	const boatRotation = manualBoat.getRotation();
	if (useMainCamera)
	{
		// Activate main camera (camera)
		// camera.position.copy(detectorCam.position);
		// camera.quaternion.copy(detectorCam.quaternion);
		orbitControls.object = orbitCam;
	} else
	{
		// Activate detectorCam
		orbitControls.target.set(
			boatPosition.x - Math.sin(boatRotation.y) * 60,  // Adjust the distance
			boatPosition.y + 25,  // Adjust the height
			boatPosition.z - Math.cos(boatRotation.y) * 60   // Adjust the distance
		);
		orbitControls.object = detectorCam;
	}
	orbitControls.update();
}
function updateAutonomousBoat()
{
	autonomousBoat.setSpeed(0.3, 0); // Autonomous boat constant forward speed
	autonomousBoat.update();
}

function animate()
{
	requestAnimationFrame(animate);
	render();
	manualBoat.update();
	updateAutonomousBoat();
	updateCamera();
}
function updateCamera()
{
	const boatPosition = manualBoat.getPosition();
	const boatRotation = manualBoat.getRotation();
	if (!useMainCamera)
	{
		orbitControls.target.set(
			boatPosition.x - Math.sin(boatRotation.y) * 65,  // Adjust the distance
			boatPosition.y + 25,  // Adjust the height
			boatPosition.z - Math.cos(boatRotation.y) * 65   // Adjust the distance
		);
		orbitControls.minDistance = 0;
		orbitControls.maxDistance = 1;
		detectorCam.rotation.y = Math.PI;
		detectorCam.lookAt(boatPosition);
	}
	else
	{
		// Update the camera position based on boat position and rotation
		orbitControls.target.set(
			boatPosition.x - Math.sin(boatRotation.y),  // Adjust the distance
			boatPosition.y + 25,  // Adjust the height
			boatPosition.z - Math.cos(boatRotation.y)   // Adjust the distance
		);
		orbitControls.minDistance = 40;
		orbitControls.maxDistance = 200;
		orbitCam.lookAt(boatPosition);
	}

	// Update OrbitControls state
	orbitControls.update();
}
function render()
{
	water.material.uniforms['time'].value += 1.0 / 60.0;
	renderer.render(scene, orbitControls.object);
}
function renderToTarget()
{
	renderer.setRenderTarget(renderTarget);
	renderer.render(scene, detectorCam);
	renderer.setRenderTarget(null); // Reset render target
}

init();
animate();
