print("=================================\nДобро пожаловать в мой калькулятор!")

while True:
  print("=================================")

  tf1 = False
  while tf1 != True:
    a = input("Введите первое число: ")
    if a.isdigit():
      a = float(a)
      tf1 = True
    else:
      print("Допущена ошибка. Попробуйте ещё раз. ")

  tf2 = False
  while tf2 != True:
    b = input("Введите второе число: ")
    if b.isdigit():
      b = float(b)
      tf2 = True
    else:
      print("Допущена ошибка. Попробуйте ещё раз. ")

  tf3 = False
  while tf3 != True:
    c = input("Введите операцию (+, -, ^, *, /: ")
    if c == "+" or c == "-" or c == "^" or c == "*" or c == "/":
      tf3 = True
    else:
      print("Допущена ошибка. Попробуйте ещё раз. ")

  if c == "+":
    print(a, "+", b, "=", a + b)
  elif c == "-":
    print(a, "-", b, "=", a - b)
  elif c == "^":
    print(a, "^", b, "=", a ** b)
  elif c == "*":
    print(a, "*", b, "=", a * b)
  elif c == "/":
    if b == 0:
      print("Делить на ноль нельзя!")
    else:
      print(a, "/", b, "=", a / b)
      if not float(a % b) == 0:
        print("Остаток от деления:", a % b)
  else:
    print("Допущена ошибка. Попробуйте ещё раз. ")