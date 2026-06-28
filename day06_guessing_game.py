#ans q21:
#        break and continue are both loop control statements, but they behave differently:
#        break: Immediately exits the loop. The program continues with the first statement after the loop.
#        continue: Skips the rest of the current iteration and moves to the next iteration of the loop.
#       for i in range(1, 11):
 #      if i == 3:
#       continue   # Skip printing 3
#       if i == 8:
#       break      # Stop the loop when i is 8
#       print(i)
#ans q22:
#       The range(start, stop, step) function in Python generates a sequence of numbers.
#       start: The first number in the sequence.
#       stop: The sequence ends before this number (the stop value is not included).
#       step: The amount by which the number increases or decreases each time. 
#       range(10, 0, -2)    generate :10, 8, 6, 4, 2
#ans q23:
#       A while loop can become an infinite loop if its condition never becomes False.
#       Two common ways to prevent this are:
#       1.Update the loop control variable 
#       2.Use a break statement
#ans q24:
#        The if, elif, and else statements are used to make decisions in a program.
#        if: Checks the first condition. If it is True, that block of code runs.
#        elif (short for "else if"): Checks another condition only if the previous if or elif conditions were False. You can have multiple elif statements.
#        else: Runs if none of the if or elif conditions are True. It is optional and does not have a condition.
import random
game_played=0
win=0
loses=0
high_score=None
 
def get_hint(number):
    hints=[]
    if number % 2 == 0:
        hints.append("the number is even.")
    else:
        hints.append("number ius odd.")
    if number % 3 ==0:
        hints.append("the number is multiple of 3.")
    if number % 5 == 0:
        hints.append("the number is multiple of 5.")
    if number % 7 == 0:
        hints.append("the number is multiple of 7.")
    if number > 100:
        hints.append("the number is greater then 100.")
    elif number < 50:
        hints.append("the number is less then 50.")
    else:
        hints.append("number is 50 or less.")
    return random.choice(hints)
while True:
    print("\n===========NUMBER GUESSING GAME============")
    print("choose a dificulty.")
    print("1.EASY 1-50 ,10 tries.")
    print("2.MEDIUM 1-100, 7 tries.")
    print("3.HARD 1-200, 5 tries.")
    while True:
         difficulty=input("enter 1,2 or 3: ")
         if difficulty =="1":
             maximum=50
             tries=10
             break
         elif difficulty=="2":
             maximum=100
             tries=7
             break
         elif difficulty=="3":
             maximum=200
             tries=5
             break
         else:
             print("invalid choice. please try again.")
    secret=random.randint(1,maximum)
    remaining=tries
    attempts_used=0
    game_played += 1
    
    print(f"\n think's that number is between 1-{maximum}.")
    print("Type 'hint' for a clue (cost 2 attempts) .")
    
    while remaining > 0:
        guess=input(f"\nGUESS! {remaining} attempts left.:")
        if guess.lower() == "hint":
            if remaining <= 2:
                print("not enough attempts remaining to use a hint.")
            remaining -= 2
            print("Hint:", get_hint(secret))  
            print("you now have {remaining} attempt left. ")
            if remaining == 0:
                break
            continue
        if not guess.isdigit():
            print("please enter a valid number.")
            continue
        guess=int(guess)
        attempts_used += 1
        remaining -= 1
        
        if guess == secret:
            print(f"\n Correct! you guessed the in {attempts_used} attempts.")
            win +=1
            if high_score is None or attempts_used < high_score:
                high_score= attempts_used
                print("New High Score")
                
            break
        elif guess < secret:
            print("Too low")
        else:
            print("too high")
            
        if remaining > 0:
            print(f"Remaining Attempts: {remaining}")
        else:
            print(f"\n Out of attempts. The number was:{secret}.")
            loses += 1
        
    if guess != secret and remaining == 0:
            if attempts_used == 0:
                print("\n The number was: {secret}.")
            loses +=0
            play_again=input("\n paly again?: (y/n)").lower()
            if play_again == "n":
                break
    print("\n=============SESSION SUMMARY==============") 
    print(f"Game played: {game_played}.")
    print(f"WIN: {win}.")
    print(f"Loses: {loses}.")
    
    if high_score is None:
        print(" Best Score: No wins yet.")
    else:
        print(f"Best Score: {high_score} in {attempts_used}")
    
    print("Thanks For Playing!.")
               
            
             
         