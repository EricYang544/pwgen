import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

using_symbols = input("Do you want to use symbols? (y/n) ")
if using_symbols == 'n':
  password_lsit = []
  for num in range(12):
    password_lsit += random.choice(numbers)

  password = "".join(password_lsit)
  print(f"Your password is '{password}'")

else:
  num_sym = numbers + symbols
  password_list = []
  for char in range(12):
    password_list += random.choice(num_sym)

  password = "".join(password_list)
  print(f"Your password is '{password}'")