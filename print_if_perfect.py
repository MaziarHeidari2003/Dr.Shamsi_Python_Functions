#PROBLEM 6


def main():
    """
    So its the main function where the user is promped for a value and we pass the value to check_if_perfect function, we are using a while loop to reprompt the user until he inputs a perfect number 
    """
    n = int(input('Enter the number: '))
    while check_if_perfect(n) == False:
      print (check_if_perfect(n))
      n = int(input('Enter the number: '))
    print(str(n)+' is a perfect number.')

def all_div(n):
    """
    this function is going to find all the devisors of a number and calculate their sum
    """
    sum = 0
    devisor = 1
    while n >= devisor:
       if n % devisor == 0:
           sum += devisor
       devisor += 1     
    return sum         

def check_if_perfect(n):
   
   """
   this function is going to use the sum of the devisors of a number by the function div_all and check if the numebr is perfect
   """
   if n == 0 :
      return False
   sum = all_div(n)
   if sum == (2 * n):
      return True
   else:
      return False

   

 
if __name__ == "__main__":  #Dear TA you could ignore this line of code.
  main()