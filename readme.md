# Poisoned Apple Game

Poisoned Apple is a simple and engaging terminal-based game where you choose between two apples, one of which is poisoned. The goal is to avoid the poisoned apple and achieve the highest score possible before meeting your untimely demise.

## Author
Vikram Kopuri
Initial commit was 100% written by me, then i used Chatgpt to help bugfix and enhance it.  

## Features

- ASCII art for an immersive retro gaming experience.
- Tracks and displays your score and best score.
- Simple and intuitive input system.

## How to Play

1. Run the game by executing the Python script.
2. At the start of each round, two apples will be displayed:
   - 🍎 (Apple 1)
   - 🍏 (Apple 2)
3. Input `1` or `2` to select an apple, or `0` to quit the game.
4. If you pick the safe apple, you score a point and move to the next round.
5. If you pick the poisoned apple, the game ends, and your score is displayed.
6. Your best score is saved across rounds until you quit the game.

## Example Gameplay

```
    __________      .__                               .___    _____                .__          
    \______   \____ |__| __________   ____   ____   __| _/   /  _  \ ______ ______ |  |   ____  
    |     ___/  _ \|  |/  ___/  _ \ /    \_/ __ \ / __ |   /  /_\  \\\____ \\\____ \|  | _/ __ \
    |    |  (  <_> )  |\___ (  <_> )   |  \  ___// /_/ |  /    |    \  |_> >  |_> >  |_\  ___/
    |____|   \____/|__/____  >____/|___|  /\___  >____ |  \____|__  /   __/|   __/|____/\___  >
                            \/           \/     \/     \/          \/|__|   |__|             \/

Poison Apple Game
=================
Two apples: one is poison. Eat the wrong apple and die.

New Game 1

  🍎     🍏
  [ 1 ]     [ 2 ]

Input 1, 2 to select apple. 0 to quit (0, 1, or 2): 1
Score: 1 | Best Score: 1

  🍎     🍏
  [ 1 ]     [ 2 ]

Input 1, 2 to select apple. 0 to quit (0, 1, or 2): 2
You ate a poisoned apple!! You died.
Score: 1 | Best Score: 1
```

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the script file.
2. Ensure Python is installed on your system.
3. Run the script:

   ```bash
   python poisoned_apple.py
   ```

## Code Overview

The script consists of:

- `display_title()`: Displays the ASCII art title.
- `random_bool()`: Randomly assigns the poison to one of the apples.
- `reset_apple()`: Resets the apple states for a new round.
- `process_print_score(score, best_score)`: Updates and displays the score.
- `display_apples()`: Displays the two apples with their labels.
- `get_input()`: Handles user input and validates it.
- `main()`: The game loop managing rounds, scores, and quitting.

## Contributions

Contributions and suggestions are welcome! Feel free to fork the repository and submit a pull request.

## License

This game is open-source and available under the MIT License.

