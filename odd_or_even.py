#PROBLEM 7


def main():
  print(even_backwards_digit(123))

  amount = int(input('How many numbers you are going to input? '))
  for i in range(amount):
    num = int(input('Number: '))


def odd_sum_digit(num):
  while num > 0:
    sum = num % 10
    num //= 10
  return sum

def even_backwards_digit(num):
  n = 0
  while num > 0:
    new_num = (num % 10) * (10 ** n)
    num //= 10
    n += 1
  return new_num


  
if __name__ == "__main__":  #Dear TA you could ignore this line of code.
  main()