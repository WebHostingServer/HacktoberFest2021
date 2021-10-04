input('Think of a number with a value between 1 to 100 then press ENTER')
print('The computer will start guessing the numbers in your mind')

lower_limit = 1
upper_limit = 100
guess = 0
guessed = False

while not guessed:
  temporary_guess = lower_limit + int((upper_limit - lower_limit)/2)
  guess = guess + 1
  
  print('Is the number {}?'.format(temporary_guess))
  response = ''

  while not (response == 'B' or response=='S' or response =='Y'):
    print("Type B if too big")
    print("Type S if too small")
    print("Type Y if right")
    response = input("Answer: ").upper()

  
  if response == 'S':
    lower_limit = temporary_guess + 1
  elif response == 'B':
    upper_limit = temporary_guess - 1
  else:
    guessed = True

print('The computer guesses the number in {} tries'.format(guess))
