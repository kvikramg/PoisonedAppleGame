from random import choice
class PoisonedApple:
    def __init__(self):
        #init variables
        self.score = 0
        self.best_score = 0
        self.quit_game = False
        self.game_no = 0
        self.run()
    
    def display_title(self):
        title_art=r"""
        __________      .__                               .___    _____                .__          
        \______   \____ |__| __________   ____   ____   __| _/   /  _  \ ______ ______ |  |   ____  
        |     ___/  _ \|  |/  ___/  _ \ /    \_/ __ \ / __ |   /  /_\  \\\____ \\\____ \|  | _/ __ \ 
        |    |  (  <_> )  |\___ (  <_> )   |  \  ___// /_/ |  /    |    \  |_> >  |_> >  |_\  ___/ 
        |____|   \____/|__/____  >____/|___|  /\___  >____ |  \____|__  /   __/|   __/|____/\___  >
                                \/           \/     \/     \/          \/|__|   |__|             \/ 

        """
        print(title_art)
        

    def random_bool(self):
        return choice([True, False])

    def reset_apple(self):
        self.apple[0] = self.random_bool()
        self.apple[1] = not self.apple[0]
        

    def process_print_score(self):
        if self.score > self.best_score:  # check for new high score
            self.best_score = self.score

        print(f'Score: {self.score} | Best Score: {self.best_score}\n')
        

    def display_apples(self):
        print("\n")
        print("   🍎         🍏         ❌")  # ASCII art for two apples
        print("  [ 1 ]      [ 2 ]      [ 0 ]")
        print("\n")

    def get_input(self):
        while True:
            try:
                self.display_apples()
                #user_input = int(input('Input 1, 2 to select apple. 0 to quit (0, 1, or 2): '))
                self.user_input = int(input('>'))
                if self.user_input in [0, 1, 2]:
                    return self.user_input
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number (0, 1, or 2).")

    def run(self):
        self.display_title()
        print('Poison Apple Game')
        print('=================')
        print('Two apples: one is poison. Eat the wrong apple and die.')



        while not self.quit_game:
            # Start a new game
            self.alive = True
            self.score = 0
            self.game_no += 1
            print(f'New Game {self.game_no}')
            
            self.apple = [True, False]  # False is the poisoned apple

            while self.alive:
                # Reset apple positions
                self.reset_apple()
                # player input
                self.get_input()

                if self.user_input == 0:
                    self.quit_game = True
                    self.alive = False
                    self.process_print_score()
                    print('👋 Bye!!')
                else:
                    self.alive = self.apple[self.user_input - 1]
                    if self.alive:
                        self.score += 1
                        print ('\U0001F60B Yummy')
                    else:
                        print('\U0001F480 You ate a poisoned apple!! You died. \U0001F480')
                    
                    self.process_print_score()

if __name__ == "__main__":
    my_game=PoisonedApple()
    
