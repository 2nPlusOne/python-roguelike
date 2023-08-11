# Python Roguelike

This project is a roguelike game developed in Python using the tcod library for making roguelike games. This project is based on the [Python roguelike tutorial](http://www.rogueliketutorials.com/tutorials/tcod/v2/) by TStand90.

## Installation and Setup

Follow these steps to get the project running on your computer:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/2nPlusOne/python-roguelike
   ```

2. **Install Python 3.7 or Higher**: You can download it from [here](https://www.python.org/downloads/).

3. **Setup a Virtual Environment**:
   Follow the instructions [here](https://docs.python.org/3/library/venv.html) to set up and run a virtual environment. You can also use tooling in VSCode or PyCharm to do this automatically.

4. **Navigate to the Project Directory and Install Dependencies**:
   ```bash
   cd python-roguelike
   pip install -r requirements.txt
   ```

5. **Install SDL2 (sometimes required depending on the system)**: Look-up and follow the instructions based on your OS.

6. **Run the Project**:
   With the virtual machine activated
   ```bash
   python main.py
   ```

   If you're using VSCode, hitting the play button at the top right (when in the main.py file) will activate the virtual environment and run the game.

## Gameplay

Wander the procedurally generated dungeon and kill all the enemies present on the map. The game is turn-based, so time only moves when you do. You can move in all four cardinal directions, and diagonally. Attacks are performed by attempting to move onto the same tile as an enemy. Keep in mind that you and all enemies can attack diagonally as well. Try to clear the dungeon before running out of health to 'win'. The win condition will change more work is done on the project.

## Controls

There are three control schemes bound (found in the input_handlers.py file), but the most intuitive are the numpad controls. For example, `7` moves up-left and `3` moves down-right. `5` will wait, effectively skipping the turn. If I continue to work on the project, I'll update this section with more detailed controls for each feature.

## Acknowledgments

Special thanks to the creators of the [Python roguelike tutorial](http://www.rogueliketutorials.com/tutorials/tcod/v2/).
