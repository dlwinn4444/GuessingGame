## Dwayne Winn CSI261 guessing game

import random
count=1
# Creating title function
def title_name():
    print('Guess the number!')
    print()
 #create main function       
def main():
 #call title function
    title_name()
    limit = int(input('What\'s the limit: '))
    print()
    #get the secret number
    r_num = random.randint( 1, limit)
    #dispaly range for guessing
    print('I\'m thinking of a number from 1 to ',limit)
    #get users input for guess
    guess = int(input('Your guess?: '))
    #start counter                    
    count=1
    # check for a correct guess
    while guess != r_num:
    #for testing   print(guess,'guess',r_num,'number')
      if guess > r_num:
        print('Too High.')
        guess = int(input('Your guess?: '))
        count += 1
      elif guess < r_num:
        print('Too Low.')
        guess = int(input('Your guess?: '))
        count += 1                              
    #display the win message
    print('You guessed it ',count,'tried.')
    replay = input('Would you like to play again? (y/n): ')
    if replay == 'y':
     main()      
    elif replay == 'n':
     print('BYE!')
     #call main function if the first run
if count ==1:
  main()
#Dwayne Winn C261 Gussing Game

                                                                                                                                                                                                                                                   


