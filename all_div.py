def main():
    """
    So its the main function where the user is promped for a value and we pass the value to all_div function
    """
    n = int(input('Enter the number: '))
    output = all_div(n)
    print(output)

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


 
if __name__ == "__main__":  #Dear TA you could ignore this line of code.
  main()