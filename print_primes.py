def main():
  """
  So its the main function where the user is promoed for a natural value
  nad then the print_prime function is being done for n times
  """
  n = int(input('Enter the natural number: '))
  for i in range(n):
    if print_prime(i):
      print(i)
  

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
  
def print_prime(x):
    """
    if x has been considered as a prime value in isprime function, this function is goint to return it
    """
    if isprime(x):
      return x
      

  
if __name__ == "__main__":  #Dear TA you could ignore this line of code.
  main()