import art
def add(n1, n2):
  return n1 + n2
def sub(n1, n2):
  return n1 - n2
def multi(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2
operations = {
  "+": add,
  "-": sub,
  "*": multi,
  "/": divide
}

def calculator():
  print(art.logo)
  print("Welcome to this pythonista calculator!")
  num1 = float(input("What's the number you want to calculate? "))
  for operator in operations:
    print(operator)
  calc_continue = True
  while calc_continue:
    operation_symbol = input("Pick an operator: ")
    num2 = float(input("What's the next number? "))
    calc_function = operations[operation_symbol]
    answer = calc_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continuation = input(f"Would you like to continue calculating with {answer}? If yes, type 'y' otherwise type 'n' to exit. ")
    if continuation == "n":
      calc_continue = False
      calculator()
    elif continuation == "y":
      num1 = answer


calculator()
