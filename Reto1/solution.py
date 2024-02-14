def problem_1(limit):
  sum = 0
  for i in range(0, limit):
    if i % 3 == 0 or i % 5 == 0:
      sum += i
  return sum

def problem_2(limit):
  fib = [1, 2]
  sum = 0
  while fib[-1] <= limit:
    if(fib[-1] % 2 == 0):
      sum += fib[-1]
    aux = fib[-1] + fib[-2]
    fib[-2] = fib[-1]
    fib[-1] = aux
  return sum

def problem_3(limit):
  return -1

def problem_4():
  num1 = 999
  num2 = 999
  while True:
    if str(num1 * num2) == str(num1 * num2)[::-1]:
      return num1 * num2
    if num1 == 100:
      num1 = 999
      num2 -= 1
    else:
      num1 -= 1

def problem_5(limit):
  min = limit
  while limit > 0:
    if min % limit == 0:
      limit -= 1
    else:
      min *= limit
  return min // 2

print(problem_3(13195))
