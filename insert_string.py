#PROBLEM 9


def main():
  """
  we input the user for three arguements used in the insert_string func nad output the results
  """
  s1 = input('Insert the fist string: ')
  s2 = input('Insert the second string: ')
  k = int(input('Where to start mixing these two strings: '))
  output = insert_string(s1,s2,k)
  print(output)



def insert_string(s1,s2,k):
  """
  this func is going to mix s1 and s2 , its going to output s1 and start s2 from the Kth position in the s1 string 
  """
  new_s = s1[:k] + s2 + s1[k:]
  return new_s



if __name__ == "__main__":  #Dear TA you could ignore this line of code.
  main()