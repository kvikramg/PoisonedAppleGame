from random import choice

class PoisonedApple:
    def __init__(self):
        # Initialize variables for game state
        self.score = 0  # Current score in the game
        self.best_score = 0  # Highest score achieved across games
        self.quit_game = False  # Flag to track if the user wants to quit
        self.game_no = 0  # Counter for the number of games played
        self.run()  # Start the game
    
    def display_title(self):
        # Display the title art for the game
        title_art = r"""
        __________      .__                               .___    _____                .__          
        \______   \____ |__| __________   ____   ____   __| _/   /  _  \ ______ ______ |  |   ____  
        |     ___/  _ \|  |/  ___/  _ \ /    \_/ __ \ / __ |   /  /_\\  \\\____ \\\____ \|  | _/ __ \ 
        |    |  (  <_> )  |\___ (  <_> )   |  \  ___// /_/ |  /    |    \  |_> >  |_> >  |_\  ___/ 
        |____|   \____/|__/____  >____/|___|  /\___  >____ |  \____|__  /   __/|   __/|____/\___  >
                                \/           \/     \/     \/          \/|__|   |__|             \/ 
        """
        print(title_art)

    def random_bool(self):
        # Randomly return True or False
        return choice([True, False])

    def reset_apple(self):
        # Randomly assign one apple as safe and the other as poisoned
        self.apple[0] = self.random_bool()
        self.apple[1] = not self.apple[0]  # Ensure one is the opposite of the other

    def process_print_score(self):
        # Update and print the current and best scores
        if self.score > self.best_score:  # Check for new high score
            self.best_score = self.score
        print(f'Score: {self.score} | Best Score: {self.best_score}\n')

    def display_apples(self):
        # Display the apple choices and their corresponding numbers
        print("\n")
        print("   🍎         🍏         ❌")  # ASCII art for apples and a quit option
        print("  [ 1 ]      [ 2 ]      [ 0 ]")
        print("\n")

    def get_input(self):
        # Get and validate user input for choosing an apple or quitting
        while True:
            try:
                self.display_apples()  # Show the apple options
                self.user_input = int(input('Input 1, 2 to select apple. 0 to quit (0, 1, or 2): '))
                if self.user_input in [0, 1, 2]:
                    return self.user_input
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number (0, 1, or 2).")

    def run(self):
        # Main game loop
        self.display_title()  # Show the game title
        print('Poison Apple Game')
        print('=================')
        print('Two apples: one is poison. Eat the wrong apple and die.')

        while not self.quit_game:
            # Start a new game instance
            self.alive = True  # Player starts alive
            self.score = 0  # Reset score for the new game
            self.game_no += 1  # Increment game counter
            print(f'New Game {self.game_no}')

            self.apple = [True, False]  # Initialize apple states (True = safe, False = poisoned)

            while self.alive:
                # Reset apple positions
                self.reset_apple()
                # Get player input
                self.get_input()

                if self.user_input == 0:  # Player chooses to quit
                    self.quit_game = True
                    self.alive = False
                    self.process_print_score()  # Display final scores
                    print('👋 Bye!!')
                else:
                    # Check if the chosen apple is safe or poisoned
                    self.alive = self.apple[self.user_input - 1]
                    if self.alive:
                        self.score += 1  # Increase score if safe apple is eaten
                        print ('\U0001F60B Yummy')  # Indicate safe choice
                    else:
                        print('\U0001F480 You ate a poisoned apple!! You died. \U0001F480')
                    
                    self.process_print_score()  # Display updated scores

if __name__ == "__main__":
    my_game = PoisonedApple()
