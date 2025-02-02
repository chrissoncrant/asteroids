# Asteroids

## Tech

-   [Pygames](https://www.pygame.org/news)

## Random Information

### The Game Loop:

Resources:

-   https://gameprogrammingpatterns.com/game-loop.html
-   https://www.makeuseof.com/gameplay-loop-gaming/

Basic Loop consists of 3 steps:

-   Check for player inputs
-   Update game world
-   Draw the game to screen

### Starting The Game:

These steps are probably specific to my own environment. I am using venv as the
virtual environment.

To activate the environment: `source venv/bin/activate` To start game:
`python3 main.py`

## Issues:

If VSCode is showing pygame as not being found, even though it is working: open
command pallete:

-   Open the Command Palette (Ctrl + Shift + P or Cmd + Shift + P on macOS).
-   Search for and select "Python: Select Interpreter."
-   Select the interpreter that matches the environment where you installed
    pygame. In my case, this is ./venv/bin/python
