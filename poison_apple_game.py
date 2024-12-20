from random import choice

def random_bool():
    return choice([True, False])

def reset_apple(a):
    a[0] = random_bool()
    a[1] = not a[0]
    return a

def process_print_score(score, best_score):
    if score > best_score:  # check for new high score
        best_score = score

    print(f'Score: {score} | Best Score: {best_score}\n')
    return best_score

def display_apples():
    print("\n")
    print("  \U0001F34E     \U0001F34F")  # ASCII art for two apples
    print("  [ 1 ]     [ 2 ]")
    print("\n")

def get_input():
    while True:
        try:
            display_apples()
            user_input = int(input('Input 1, 2 to select apple. 0 to quit (0, 1, or 2): '))
            if user_input in [0, 1, 2]:
                return user_input
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number (0, 1, or 2).")

def main():
    print('Poison Apple Game')
    print('=================')
    print('Two apples: one is poison. Eat the wrong apple and die.')

    score = 0
    best_score = 0
    quit_game = False
    game_no = 0

    while not quit_game:
        # Start a new game
        alive = True
        score = 0
        game_no += 1
        print(f'New Game {game_no}')
        
        apple = [True, False]  # False is the poisoned apple

        while alive:
            # Reset apple positions
            apple = reset_apple(apple)
            user_input = get_input()

            if user_input == 0:
                quit_game = True
                alive = False
                best_score = process_print_score(score, best_score)
                print('Bye!!')
            else:
                alive = apple[user_input - 1]
                if alive:
                    score += 1
                else:
                    print('You ate a poisoned apple!! You died.')
                
                best_score = process_print_score(score, best_score)

if __name__ == "__main__":
    main()
