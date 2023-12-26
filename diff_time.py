#PROBLEM 8

def main():
  print('Some examples for the right format to input the times: 3:45 PM or 2:5 AM or 10:0 PM')
  continue_check = 'Y'
  while continue_check == 'Y':
    time1 = input('enter the first exact time: ')
    time2 = input('enter the second exact time: ')
    hour1,min1,am_pm1 = split(time1)
    hour2,min2,am_pm2 = split(time2)
    diff = diff_time(hour1,min1,am_pm1,hour2,min2,am_pm2)
    print(diff)
    while True:
      continue_check = input('Do you want to continue? Y or N: ')
      if continue_check == 'Y' or continue_check == 'N':
        break
      print('Invalid input')



def split(time):
  j = 0
  for i in range(len(time)):
    if time[i] == ':':
      hour = time[:i]
      j = i
    if time[i] == ' ':
      min = time[j+1:i]
      if time[i+1:] == 'AM':
        am_pm = True
      elif time[i+1:] == 'PM':
        am_pm = False    
  return int(hour),int(min),am_pm      



def my_abs(x,y):
  if x >= y :
    z = x - y
  else:
    z = y - x
  return z  


def diff_time(hour1,min1,am_pm1,hour2,min2,am_pm2): 
  if am_pm1 == False:
    hour1 += 12
  if am_pm2 == False:
    hour2 += 12
  diff = (hour2 * 60 + min2 )  - (hour1 * 60 + min1)
  return diff



if __name__ == "__main__":  #Dear TA you could ignore this line of code.
  main()
      

