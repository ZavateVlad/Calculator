new_calculation = True
def calculator(first_number, pick_op, second_number):
  new_number = 0

  if pick_op == symbols[0]:
    new_number = first_number + second_number
  elif pick_op == symbols[1]:
    new_number = first_number - second_number
  elif pick_op == symbols[2]:
    new_number = first_number * second_number
  elif pick_op == symbols[3]:
    new_number = first_number / second_number

  return new_number
  
first = float(input("What's your first number?: "))

while new_calculation:
  symbols = ['+', '-', '*', '/']
  
  for sign in symbols:
    print(sign)
    
  op = input("Pick operation: ")
  second = float(input("What's your next number?: "))
  last_number = calculator(first, op, second)
  print(f"{first} {op} {second} = {last_number}")
  new = input(f"Type 'y' to continue calculating with {last_number}, or type 'n' to start new calculation: ").lower()
  
  if new == 'y':
    first = last_number
  elif new =='n':
    first = int(input("What's your first number?: "))
    calculator(first, op, second)
