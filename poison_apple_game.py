'''
Poison apple game
no depenency except std
Two apple, one is poison, eat the wrong apple and die
Input 1,2 to select apple 
0 to quit
''' 

from random import choice

def random_bool():
    return choice([True,False])

def reset_apple(a):
    a[0]=random_bool()
    a[1]=not a[0]
    return a

def process_print_score(score,best_score):
    if score>best_score: #check for new high score
        best_score=score

    print(f'Score: {score} |Best Score: {best_score} \n')
    return best_score

def get_input():
    return (int(input("Input 1,2 to select apple. 0 to quit (0,1 or 2):")))

def main():
    print('Poison Apple Game', end='\n')
    print('=================', end='\n')
    print('Two apple, one is poison, eat the wrong apple and die', end='\n')
    #print('Input 1,2 to select apple. 0 to quit', end='\n')
    score=0
    best_score=0
    alive=True
    quit=False
    apple=[True,False] #false is poisoned apple
    
    input=1
    game_no=0



    while not quit:
        #reset
        alive=True
        score=0
        game_no=game_no+1
        print(f'New Game {game_no}', end='\n')
        while alive:
            #reset apple
            apple=reset_apple(apple)
            input=get_input()
            if input==0:
                quit=True
                alive=False
                best_score=process_print_score(score,best_score)
                print('Bye!!',end='\n')
            else:
                alive=apple[input-1]
                if alive:
                    score=score+1                    
                else:
                    print('You ate Poisoned apple!! You Died',end='\n')
                best_score=process_print_score(score,best_score)
                    
                
    
    


if __name__=="__main__":
    main()

