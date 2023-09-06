# Modelo 3D

## Inclusão da Biblioteca Three.js:

O código inclui a biblioteca Three.js através de um script. Essa biblioteca é usada para criar gráficos 3D em um navegador web.

## Criação da Cena:

const scene = new THREE.Scene();: Cria uma cena onde todos os objetos 3D serão colocados.

## Criação da Câmera:

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);: Cria uma câmera de perspectiva, que simula a visão de uma pessoa. Os parâmetros definem o campo de visão (75 graus), a razão de aspecto (baseada na janela do navegador), a distância mínima e máxima de renderização.

## Criação do Renderizador:

const renderer = new THREE.WebGLRenderer();: Cria um renderizador WebGL para exibir a cena.
renderer.setSize(window.innerWidth, window.innerHeight);: Define o tamanho da área de renderização para corresponder à janela do navegador.
document.body.appendChild(renderer.domElement);: Adiciona o elemento de renderização ao corpo do documento HTML.

## Geometria e Texturas:

O código define geometrias (pirâmide, cubo e esfera) e carrega texturas para cada uma delas. As texturas são imagens que serão aplicadas aos objetos 3D.

## Materiais e Malhas:

Cria materiais para os objetos 3D, utilizando as texturas carregadas anteriormente.
const pyramid = new THREE.Mesh(pyramidGeometry, pyramidMaterial);: Cria uma malha (ou mesh) da pirâmide utilizando a geometria e o material.
scene.add(pyramid);: Adiciona a pirâmide à cena.

## Criação de Outros Objetos:

O código cria um cubo e uma esfera da mesma maneira que a pirâmide.

## Posições Iniciais:

Define as posições iniciais para o cubo e a esfera, especificando suas coordenadas (x, y, z) em relação à cena.

## Configuração da Câmera:

Define a posição inicial da câmera no espaço 3D.

## Animação:

A função animate() é chamada repetidamente usando requestAnimationFrame(). Ela é responsável por animar os objetos na cena.
Neste caso, a pirâmide é girada continuamente nos eixos X e Y.

O cubo e a esfera também são animados para se moverem circularmente ao redor da pirâmide central.

## Renderização:

A função renderer.render(scene, camera); renderiza a cena com a câmera atual e a exibe no elemento de renderização.

# Resultado

![image](https://github.com/luscipher/ComputaGrafica/assets/122156760/26c47ff1-2890-4f6e-b66e-d2c937355470)
