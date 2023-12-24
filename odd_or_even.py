#PROBLEM 7


def main():
  amount = int(input('How many numbers you are going to input? '))
  for i in range(amount):
    num = int(input('Number: '))
    if num % 2 == 0:
      print(even_backwards_digit(num))
    else:
      print(odd_sum_digit(num))


def odd_sum_digit(num):
  sum = 0
  while num > 0:
    sum += num % 10
    num //= 10
  return sum

def even_backwards_digit(num):
  new_num = 0
  while num > 0:
    new_num = (num % 10)+ new_num * 10
    num //= 10
  return new_num


  
if __name__ == "__main__":  #Dear TA you could ignore this line of code.
  main()