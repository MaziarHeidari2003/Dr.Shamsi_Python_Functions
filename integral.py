#PROBLEM 10


def func(x):
  """
  its just a random mathematical func ,
  we are going to use it to calcualate the integral
  """
  return 2*x+1


def integral(a,b,n,func):

  """
  calaulates the integral. we should calcaulate the steps , we should use trapezoid method to calculate the integral
  """
  sum = 0
  step = my_abs((a-b)) / n
  x = a
  while x < b:
    if x == 0 or x == n:
      sum += func(x)/2
    else:  
      sum += func(x) 
    x += step
  result = sum * step 
  return result


  
def my_abs(x):
  """
    these function will return the absolute 
    value of x  so that we 
    dont have to deal with nagetive values
  """
  if x >= 0 :
    return x
  else:
    return -x
    


result = integral(0,7,1000000,func)
print(result)