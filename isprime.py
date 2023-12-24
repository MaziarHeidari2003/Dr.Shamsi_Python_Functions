#PROBLEM 1

def main():
  """
  So its the main function where the user is promoed for a natural value
  nad then the isprime function is being done
  """
  n = int(input('Enter the natural number: '))
  
  output = isprime(n)
  print(output)

def isprime(x):
  """
  Checks if a number is prime(returns True) or not(returns False)
  """
  y = 2
  if x != 1 :
    while x != y and x % y != 0:
      y += 1
    return x == y   
  else:
    return False   


if __name__ == "__main__":  #Dear TA you could ignore this line of code.
  main()