# Snake Game README
This is a simple Snake Game implemented in JavaScript using the HTML5 Canvas element. In this game, you control a snake that moves around the canvas and tries to eat food to grow in size. The game ends if the snake collides with the canvas boundaries or itself.

## Code Overview
Here's an overview of the JavaScript code used to create the Snake Game:

## Constants and Variables
gameBoard: Represents the canvas where graphics are drawn.
ctx: Provides the 2D rendering context for drawing on the canvas.
scoreText: Displays the player's score.
resetBtn: Allows the player to reset the game.
gameWidth and gameHeight: Define the dimensions of the game canvas.
boardBackground, snakeColor, snakeBorder, and foodColor: Define colors used in the game.
unitSize: Represents the size of each unit (snake segment and food).

## Game State Variables
running: Tracks whether the game is currently running.
xVelocity and yVelocity: Determine the snake's movement direction.
foodX and foodY: Store the coordinates of the food.
score: Keeps track of the player's score.

## Snake and Food
snake: An array representing the snake's body, starting with one segment.
createFood(): Generates random coordinates for the food.
drawFood(): Draws the food on the canvas.

## Game Loop
gameStart(): Initializes the game state and starts the game loop.
nextTick(): Implements the game loop, updating the canvas and checking for game over conditions.

## Drawing Functions
clearBoard(): Clears the canvas.
moveSnake(): Moves the snake, adds new segments, and checks for food consumption.
drawSnake(): Draws the snake on the canvas.

## Event Listeners
window.addEventListener("keydown", changeDirection): Listens for arrow key presses to change the snake's direction.
resetBtn.addEventListener("click", resetGame): Listens for the "Reset" button click to start a new game.

## Game Over Handling
checkGameOver(): Checks if the game is over based on collision conditions.
displayGameOver(): Displays a "GAME OVER!" message on the canvas when the game ends.

## Resetting the Game
resetGame(): Resets the game to its initial state.
Feel free to explore and modify the code to enhance the game or add new features. Enjoy playing the Snake Game!
