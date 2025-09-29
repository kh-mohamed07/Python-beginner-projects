import random
play_again="yes"
while play_again.lower()=='yes':
    user_or_computer=input('which version do you want to play?(computer/user)')
    if user_or_computer.lower()=='computer':
        attempts=1
        number=random.choice(range(101))
        while True:
            try:
                user_input=int(input("Please enter your guess (from 0 to 100) "))
                if 0 <= user_input <= 100:
                    break
                else:
                    print("Please enter a number between 0 and 100.")
            except ValueError:
                print("That's not a valid number. Please try again.")
        while user_input != number :
            if user_input<number :
                if number-user_input>20:
                    print("your guess is too low")
                else:
                    print("your guess is lower than the number to guess")
            elif user_input>number:
                if user_input-number>20 :
                    print("your guess is too high")
                else: 
                    print("your guess is higher than the number to guess")
            while True:
                try:
                    user_input=int(input("Try again (from 0 to 100) "))
                    if 0 <= user_input <= 100:
                        break
                    else:
                        print("Please enter a number between 0 and 100.")
                except ValueError:
                    print("That's not a valid number. Please try again.") 
            attempts+=1
            if attempts==10:
                print("You have exceeded the allowed number of attempts.")
                break
        if user_input==number:
            if attempts==1:
                print(f"Congrats!! your guess is correct , you did it in {attempts} attempt")
            else: 
               print(f"Congrats!! your guess is correct , you did it in {attempts} attempts")


    elif user_or_computer.lower()=='user':
        attempts=1
        low=0
        high=101
        feedback=''
        while feedback != 'C':
            number=random.choice(range(low,high))
            feedback=input(f"the number u think about is {number}??[type (C) if it's correct , (H) if it's high , (L) if it's low]")
            if feedback=='C':
                print(f'yeeess I guess it , i did it in {attempts} attempts')
            elif feedback=='H':
                high=number
            elif feedback=='L':
                low=number+1
            attempts+=1
    print('just ')

    play_again=input('do u want to play again?? (yes/no)')