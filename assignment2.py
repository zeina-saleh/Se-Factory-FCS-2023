#### QUESTION1 ####
def reverseString(s,i):
  str = ''
  for ch in s:
    str = ch + str
  print(str*i)

#### QUESTION2 ####
def rearrangeString(s):
  str_upper = ''
  str_lower = ''
  for ch in s:
    if ch!=' ':
      if ch.isupper():
        str_upper += ch
      else:
        str_lower += ch
  print(str_upper+str_lower)

#### QUESTION3 ####
def checkStrings(s1,s2):
  str = ''
  if len(s1)==len(s2):
    for ch in s1:
      if ch in s2:
        str += ch
  if len(str)==len(s2):
    #print(True)
    return True
  else:
    #print(False)
    return False

#### QUESTION4 ####
def getMaxMin(l):
  max = l[0]
  min = l[0]
  for i in range(0, len(l)):
    if l[i] > max:
      max = l[i]
      index_max = i
    elif l[i] < min:
      min = l[i]
      index_min = i
  print('the highest value in the list is',max,
'at index',index_max)
  print('the lowest value in the list is',min,
'at index',index_min)

#### QUESTION5 ####
def sumDigits(n):
  if n==0:
    return 0
  result = n%10
  return result + sumDigits(n//10)

#### QUESTION6 ####
  

#### QUESTION7 ####
def reverseNumber(n):
  if n==0:
    return 0
  exponent = len(str(n))
  result = n%10
  operand = pow(10, exponent-1)
  return result*operand + reverseNumber(n//10)
      
    