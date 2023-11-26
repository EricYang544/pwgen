import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

using_symbols = input("Do you want to use symbols? (y/n): ")
pw_length = int(input("(If you enter 0, the program will generate 12 digits password.)\nHow many digits do you want for your password?: "))

if pw_length == 0:
  if using_symbols == 'n':
    password_lsit = []
    for num in range(12):
      password_lsit += random.choice(numbers)
  
    password = "".join(password_lsit)
    print(f"Your password is '{password}'")
  
  elif using_symbols == 'y':
    num_sym = numbers + symbols
    password_list = []
    for char in range(12):
      password_list += random.choice(num_sym)
  
    password = "".join(password_list)
    print(f"Your password is '{password}'")

  else:
    print("You have to enter 'y' or 'n'." )
    quit()

elif pw_length != 0:
  if using_symbols == 'n':
    password_lsit = []
    for num in range(0,pw_length):
      password_lsit += random.choice(numbers)

    password = "".join(password_lsit)
    print(f"Your password is '{password}'")

  elif using_symbols == 'y':
    num_sym = numbers + symbols
    password_list = []
    for char in range(0, pw_length):
      password_list += random.choice(num_sym)

    password = "".join(password_list)
    print(f"Your password is '{password}'")

  else:
    print("You have to enter 'y' or 'n'." )
    quit()

else:
  print("You have to enter a number.")
  quit()