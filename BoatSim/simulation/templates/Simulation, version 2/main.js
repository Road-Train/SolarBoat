import './style.css';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { Water } from 'three/examples/jsm/objects/Water.js';
import { Sky } from 'three/examples/jsm/objects/Sky.js';
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader';

let orbitCam, detectorCam, scene, renderer;
let orbitControls, water, sun;
let leftCamera, rightCamera;
let cameras = []
let activeCam = 0;
let manualBoat, autonomousBoat, demoBoat;
const objLoader = new OBJLoader();
const fbxLoader = new FBXLoader();
const buoys = [];

class Boat
{
	constructor(startPosition, addCameras)
	{
		this.velocity = 0;
		this.rotationSpeed = 0;
		this.targetVel = 0;
		this.targetRot = 0;
		this.acceleration = 0.02;
		this.boat = null;
		fbxLoader.load('/assets/boat/sail.fbx', (fbx) =>
		{
			fbx.traverse(function (child) 
			{
				if (child instanceof THREE.Mesh) 
				{
					child.material.side = THREE.DoubleSide;
				}
			});

			fbx.scale.set(0.025, 0.025, 0.025);
			fbx.position.set(0, 0, 0);

			this.boat = new THREE.Object3D();
			this.boat.position.copy(startPosition);
			this.boat.rotation.y = 1.5;
			this.boat.add(fbx);
			scene.add(this.boat);

			if (addCameras) 
			{
				this.addCameras();
			}
		});
	}
	addCameras()
	{
		orbitCam = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 1, 20000);
		leftCamera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000);
		rightCamera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000);
		detectorCam = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000);
		cameras = [orbitCam, detectorCam];

		orbitCam.position.set(0, 30, -30);
		detectorCam.position.set(0, 30, -60);
		leftCamera.position.set(-5, 30, -60);
		rightCamera.position.set(5, 30, -60);

		this.boat.add(orbitCam);
		this.boat.add(detectorCam);
		this.boat.add(leftCamera);
		this.boat.add(rightCamera);
		orbitControls = new OrbitControls(orbitCam, renderer.domElement);
		orbitControls.maxPolarAngle = Math.PI * 0.495;
		orbitControls.target.copy(this.boat.position);
		orbitControls.target.y += 30;
		orbitControls.minDistance = 60.0;
		orbitControls.maxDistance = 200.0;
		scene.add(orbitControls);
		orbitControls.update();
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

function init()
{
	scene = new THREE.Scene();
	manualBoat = new Boat(new THREE.Vector3(5, -18, 50), true);  // Keyboard-controlled boat
	demoBoat = new Boat(new THREE.Vector3(-200, -18, 50), false);  // Stationary boat for object recognition demo.
	// autonomousBoat = new Boat(new THREE.Vector3(10, -18, 55),false); // Autonomous boat
	renderer = new THREE.WebGLRenderer();
	renderer.setPixelRatio(window.devicePixelRatio);
	renderer.setSize(window.innerWidth, window.innerHeight);
	renderer.toneMapping = THREE.ACESFilmicToneMapping;
	document.body.appendChild(renderer.domElement);

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

	window.addEventListener('resize', onWindowResize);
	window.addEventListener('keydown', onKeyDown);
	window.addEventListener('keyup', onKeyUp);
	let buoyCoords = [[700, -5, 250], [-400, -5, -100], [50, -5, -20]]
	for (let i = 0; i < buoyCoords.length; i++)
	{
		objLoader.load('/assets/boat/Low_Poly_Buoy.obj', (obj) =>
		{
			obj.traverse(function (child)
			{
				if (child instanceof THREE.Mesh)
				{
					child.material.side = THREE.DoubleSide;
				}
			});

			obj.scale.set(5, 5, 5);
			obj.position.set(buoyCoords[i][0], buoyCoords[i][1], buoyCoords[i][2]); // Adjust the position as needed
			scene.add(obj);
			buoys.push(obj);
		});
	}

	// Add Ambient Light
	const ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // soft white light
	scene.add(ambientLight);

	// Add Directional Light
	const directionalLight = new THREE.DirectionalLight(0xffffff, 1); // white light
	directionalLight.position.set(50, 50, 50);
	directionalLight.castShadow = true;
	scene.add(directionalLight);
	connectWebSocket();
	animate();
}
// Function to capture an image and split it into chunks
async function captureAndSendImageChunks(camera, websocket, chunkSize = 16384)
{
	renderer.render(scene, camera);
	const imageData = renderer.domElement.toDataURL('image/png').split(',')[1]; // Base64 encoded image data
	const totalChunks = Math.ceil(imageData.length / chunkSize);

	for (let i = 0; i < totalChunks; i++)
	{
		let cameraId;
		switch (camera)
		{
			case leftCamera:
				cameraId = 'left';
				break;
			case rightCamera:
				cameraId = 'right';
				break;
			case detectorCam:
				cameraId = 'center';
				break;
		}
		const chunk = imageData.slice(i * chunkSize, (i + 1) * chunkSize);
		await websocket.send(JSON.stringify({
			cameraId, chunk, index: i, total: totalChunks
		}));
	}
}

// Function to capture images from both cameras and send them in chunks
async function connectWebSocket()
{
	const websocket = new WebSocket('ws://localhost:8765');
	let sendImagesInterval;
	websocket.onopen = async () =>
	{
		sendImagesInterval = setInterval(async () =>
		{
			await captureAndSendImageChunks(detectorCam, websocket);
			await captureAndSendImageChunks(leftCamera, websocket);
			await captureAndSendImageChunks(rightCamera, websocket);
		}, 200);
	};

	websocket.onmessage = (event) =>
	{
		const message = JSON.parse(event.data);
		console.log(message.status); // Handle server responses if needed
	};

	websocket.onerror = (error) =>
	{
		console.error('WebSocket Error: ', error);
		clearInterval(sendImagesInterval);
	};

	websocket.onclose = () =>
	{
		console.log('WebSocket connection closed');
		clearInterval(sendImagesInterval);
	};
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
	activeCam++;
	if (activeCam >= cameras.length + 1)
	{
		activeCam = 0;
	}
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
	// updateAutonomousBoat();
	updateCamera();
}

function updateCamera()
{
	const boatPosition = manualBoat.getPosition();
	const boatRotation = manualBoat.getRotation();
	// Update the camera position based on boat position and rotation
	orbitControls.target.set(
		boatPosition.x - Math.sin(boatRotation.y),  // Adjust the distance
		boatPosition.y + 30,  // Adjust the height
		boatPosition.z - Math.cos(boatRotation.y)   // Adjust the distance
	);
	// Update OrbitControls state
	orbitControls.update();
}
function render()
{
	water.material.uniforms['time'].value += 1.0 / 60.0;
	if (activeCam >= cameras.length)
	{
		// Render scene from both cameras (for verification)
		renderer.setViewport(0, 0, window.innerWidth / 2, window.innerHeight);
		renderer.setScissor(0, 0, window.innerWidth / 2, window.innerHeight);
		renderer.setScissorTest(true);
		renderer.render(scene, leftCamera);

		renderer.setViewport(window.innerWidth / 2, 0, window.innerWidth / 2, window.innerHeight);
		renderer.setScissor(window.innerWidth / 2, 0, window.innerWidth / 2, window.innerHeight);
		renderer.setScissorTest(true);
		renderer.render(scene, rightCamera);
	}
	else
	{
		renderer.setSize(window.innerWidth, window.innerHeight);
		renderer.setScissorTest(false);
		renderer.render(scene, cameras[activeCam]);
	}
}
init();