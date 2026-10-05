# Pong Game

A classic Pong game built in Python using the Turtle graphics library. This project was created as part of my Python learning journey and focuses on object-oriented programming, game logic, keyboard controls, collision detection, and working with multiple classes.

## Features

* Two-player Pong game
* Player-controlled paddles
* Keyboard controls for both players
* Ball movement and bouncing
* Collision detection with walls and paddles
* Score tracking
* Ball reset after a player misses
* Increasing ball speed after paddle collisions
* Paddle movement restricted to the screen boundaries

## Technologies Used

* Python
* Turtle Graphics
* Object-Oriented Programming (OOP)

## Controls

### Right Paddle

* `Up Arrow` — Move up
* `Down Arrow` — Move down

### Left Paddle

* `W` — Move up
* `S` — Move down

## Project Structure

```text
Pong/
│
├── main.py
├── paddle.py
├── ball.py
├── scoreboard.py
└── README.md
```

### `main.py`

Creates the game screen and brings the different game components together. It controls the main game loop and handles ball movement, collisions, scoring, and game updates.

### `paddle.py`

Contains the `Paddle` class, which inherits from Python's `Turtle` class. It controls paddle creation, movement, keyboard input, and screen boundaries.

### `ball.py`

Contains the `Ball` class. It controls ball movement, wall and paddle collisions, ball speed, and resetting the ball after a player misses.

### `scoreboard.py`

Contains the `Scoreboard` class, which keeps track of both players' scores and displays them on the screen.

## Object-Oriented Programming

This project uses several OOP concepts:

* **Classes and objects** — `Ball`, `Paddle`, and `Scoreboard`
* **Inheritance** — `Ball`, `Paddle`, and `Scoreboard` inherit from `Turtle`
* **Methods** — Game behaviour is organised into methods such as `move()`, `bounce_x()`, `bounce_y()`, and `check_collision_with_paddle()`
* **Encapsulation** — Each class is responsible for its own behaviour and data

For example:

```python
class Ball(Turtle):
    def __init__(self):
        super().__init__()
```

The `Ball` class inherits functionality from Python's built-in `Turtle` class.

## How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/vanitatech/Pong.git
```

Navigate into the project directory:

```bash
cd Pong
```

Run the game:

```bash
python main.py
```

On some systems, you may need to use:

```bash
python3 main.py
```

## What I Learned

Through this project, I practised:

* Creating classes and objects in Python
* Using inheritance with the Turtle library
* Handling keyboard events
* Building a game loop
* Detecting collisions
* Working with coordinates and movement
* Managing game state
* Separating functionality across multiple Python files
* Using methods to organise and reuse code

## Future Improvements

Possible improvements include:

* Adding a start screen
* Adding a game-over condition
* Adding sound effects
* Adding different difficulty levels
* Adding a pause function
* Adding more advanced ball physics
* Adding a single-player mode with an AI-controlled paddle

## Project

This project is part of my Python learning and portfolio development journey.
