import random

randomnum = random.randint(1,9)
guesses = 1

print("I have a secret number, can you guess  what it is?")
print("Its a number between 1 and 9 \n")
  
while True:

  userguess = input("")
  userguess = int(userguess)
  if userguess > randomnum :
    print("its too high")

    False
  elif userguess < randomnum:
    print("its too low")

    False
  else:
    print("You guessed it!")
    print("It took you ", guesses , "guesses")

  guesses += 1
exit = input("Would like to try again? Y or N \n")

if exit=="Y" :
      True
elif exit == "N":
      print("Thank you")
      False
