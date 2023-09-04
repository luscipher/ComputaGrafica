// Criação da cena
const scene = new THREE.Scene();
// Criação da câmera
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

// Criação do renderizador
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Criação da geometria da pirâmide (diminuída)
const pyramidGeometry = new THREE.ConeGeometry(1, 2, 4); // Diminui o tamanho
// Material vermelho para a pirâmide
const pyramidMaterial = new THREE.MeshBasicMaterial({ color: 0xff0000 });
const pyramid = new THREE.Mesh(pyramidGeometry, pyramidMaterial);
scene.add(pyramid);

// Criação do cubo
const cubeGeometry = new THREE.BoxGeometry(0.4, 0.4, 0.4);
// Material para o cubo
const cubeMaterial = new THREE.MeshBasicMaterial({ color: 0x228}); // Cores Pantone
const cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
cube.position.set(2, 0, 2); // Posição inicial do cubo
scene.add(cube);

// Criação da esfera 
const sphereGeometry = new THREE.SphereGeometry(0.2, 32, 32);
// Material para a esfera 
const sphereMaterial = new THREE.MeshBasicMaterial({ color: 0x800080 }); // Roxo
const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
sphere.position.set(-2, 0, -2); // Posição inicial da esfera
scene.add(sphere);

// Configuração da posição da câmera
camera.position.z = 10;

// Função de animação para girar todas as formas
const animate = () => {
    requestAnimationFrame(animate);

    pyramid.rotation.x += 0.01;
    pyramid.rotation.y += 0.01;

    // Girar o cubo ao redor da pirâmide central
    cube.position.x = 2 * Math.cos(Date.now() * 0.001);
    cube.position.z = 2 * Math.sin(Date.now() * 0.001);

    // Girar a esfera ao redor da pirâmide central
    sphere.position.x = -2 * Math.cos(Date.now() * 0.001);
    sphere.position.z = -2 * Math.sin(Date.now() * 0.001);

    renderer.render(scene, camera);
};

animate();