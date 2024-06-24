import './style.css';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { Water } from 'three/examples/jsm/objects/Water.js';
import { Sky } from 'three/examples/jsm/objects/Sky.js';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js';

let camera, scene, renderer;
let controls, water, sun;

const loader = new OBJLoader();
const buoys = [];

class Boat {
  constructor(startPosition) {
    this.speed = {
      vel: 0,
      rot: 0
    };

    loader.load("/assets/boat/sail.obj", (obj) => {
      obj.traverse(function (child) {
        if (child instanceof THREE.Mesh) {
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

  stop() {
    this.speed.vel = 0;
    this.speed.rot = 0;
  }

  update() {
    if (this.boat) {
      this.avoidBuoys();
      this.boat.rotation.y += this.speed.rot;
      this.boat.translateZ(this.speed.vel);
    }
  }

  setSpeed(vel, rot) {
    this.speed.vel = vel;
    this.speed.rot = rot;
  }

  avoidBuoys() {
    if (!this.boat) return;

    buoys.forEach(buoy => {
      const distance = this.boat.position.distanceTo(buoy.position);
      if (distance < 15) { // If within 15 units of a buoy
        const angleToBuoy = Math.atan2(
          buoy.position.z - this.boat.position.z,
          buoy.position.x - this.boat.position.x
        );

        // Calculate a direction to steer away from the buoy
        const avoidAngle = angleToBuoy + Math.PI / 2; // Perpendicular to the direction to the buoy

        this.boat.rotation.y = avoidAngle;
      }
    });
  }
}

// Initialize two boats with different starting positions
const boat1 = new Boat(new THREE.Vector3(5, -18, 50));  // Keyboard-controlled boat
const boat2 = new Boat(new THREE.Vector3(10, -18, 55)); // Autonomous boat

function init() {
  renderer = new THREE.WebGLRenderer();
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  document.body.appendChild(renderer.domElement);

  scene = new THREE.Scene();

  camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 1, 20000);
  camera.position.set(30, 30, 100);

  sun = new THREE.Vector3();

  const waterGeometry = new THREE.PlaneGeometry(10000, 10000);
  water = new Water(
    waterGeometry,
    {
      textureWidth: 512,
      textureHeight: 512,
      waterNormals: new THREE.TextureLoader().load('assets/waternormals.jpg', function (texture) {
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

  function updateSun() {
    const phi = THREE.MathUtils.degToRad(90 - 2);
    const theta = THREE.MathUtils.degToRad(180);

    sun.setFromSphericalCoords(1, phi, theta);

    sky.material.uniforms['sunPosition'].value.copy(sun);
    water.material.uniforms['sunDirection'].value.copy(sun).normalize();

    scene.environment = pmremGenerator.fromScene(sky).texture;
  }

  updateSun();

  controls = new OrbitControls(camera, renderer.domElement);
  controls.maxPolarAngle = Math.PI * 0.495;
  controls.target.set(0, 10, 0);
  controls.minDistance = 40.0;
  controls.maxDistance = 200.0;
  controls.update();

  window.addEventListener('resize', onWindowResize);
  window.addEventListener('keydown', onKeyDown);
  window.addEventListener('keyup', onKeyUp);

  // Load and add the first buoy to the scene
  loader.load('/assets/boat/Low_Poly_Buoy.obj', (obj) => {
    obj.traverse(function (child) {
      if (child instanceof THREE.Mesh) {
        child.material.side = THREE.DoubleSide;
      }
    });

    obj.scale.set(5, 5, 5);
    obj.position.set(700, -5, 250); // Adjust the position as needed
    scene.add(obj);
    buoys.push(obj);
  });

  // Load and add the second buoy to the scene
  loader.load('/assets/boat/Low_Poly_Buoy.obj', (obj) => {
    obj.traverse(function (child) {
      if (child instanceof THREE.Mesh) {
        child.material.side = THREE.DoubleSide;
      }
    });

    obj.scale.set(5, 5, 5);
    obj.position.set(-400, -5, -100); // Adjust the position as needed
    scene.add(obj);
    buoys.push(obj);
  });

  // Load and add the third buoy to the scene
  loader.load('/assets/boat/Low_Poly_Buoy.obj', (obj) => {
    obj.traverse(function (child) {
      if (child instanceof THREE.Mesh) {
        child.material.side = THREE.DoubleSide;
      }
    });

    obj.scale.set(5, 5, 5);
    obj.position.set(50, -5, -20); // Adjust the position as needed
    scene.add(obj);
    buoys.push(obj);
  });
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

function onKeyDown(event) {
  switch (event.key) {
    case 'ArrowUp':
      boat1.setSpeed(1.0, 0); // Move forward
      break;
    case 'ArrowDown':
      boat1.setSpeed(-1.0, 0); // Move backward
      break;
    case 'ArrowLeft':
      boat1.setSpeed(0, 0.1); // Turn left
      break;
    case 'ArrowRight':
      boat1.setSpeed(0, -0.1); // Turn right
      break;
  }
}

function onKeyUp(event) {
  switch (event.key) {
    case 'ArrowUp':
    case 'ArrowDown':
      boat1.setSpeed(0, 0); // Stop moving
      break;
    case 'ArrowLeft':
    case 'ArrowRight':
      boat1.setSpeed(0, 0); // Stop rotating
      break;
  }
}

function updateAutonomousBoat() {
  boat2.setSpeed(0.5, 0); // Move forward constantly without rotating
  boat2.update();
}

function animate() {
  requestAnimationFrame(animate);
  render();
  boat1.update();
  updateAutonomousBoat();
}

function render() {
  water.material.uniforms['time'].value += 1.0 / 60.0;
  renderer.render(scene, camera);
}

init();
animate();
