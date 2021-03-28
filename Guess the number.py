import random

def clue_type(num):
    print(num)
    if num%2 == 0:
        print('Clue: It is a Even number')
        
    else:
        print('It is a Odd number')

        

play =  input ( 'Play (Y/N)? :' )

if play == 'y' or play == 'Y':
    rand_number = random.randrange(1,10)
    score = 10
    clue_type(rand_number)

    while score in range(1,11):
        guess = input('Guess the number : ')
        print (rand_number)
        print (guess)

        if int(guess) is rand_number :
            print ('Congrats! You have guessed correctly')
            print ('Your Score: ',score)
            exit
        else:
            print ('Sorry! You have guessed wrongly')
            score = score - 2
            print ('Your Score: ',score)


else:
    exit





        
