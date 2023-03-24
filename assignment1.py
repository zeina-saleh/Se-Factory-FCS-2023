#### QUESTION1 ####
#a. 10*(90+2)-5 = 915
#b. 10*90+2-5 = 897
#c. 10*90+(2-5) = 897
#d. 10.0*(90+2)-5 = 915.0
#e. 120/(20+40)-(6-2)/4 = 1.0
#f. 5.0/2 = 2.5
#g. 5/2 = 2.5
#h. 5.0/2.0 = 2.5
#i. 5/2.0 = 2.5
#j. 678%3*(8-(9/4)) = 0.0

i=0
while i<1:
  equation= input('enter 1st   side of equation: ')
  result= eval(equation)
  print(equation," = ",result)
  i+=1
print('')
  
#### QUESTION2 ####
id = input('enter your ID: ')
name = input('enter your name: ').upper()
birth_date = input('enter your birth date: ')
date = birth_date.split('-')
address = input('enter your address: ').lower()

print('Your profile - ID: '+'0'+id)
print('Name: '+name)

print('DOB: ', end='')
if len(date)!=1:
  print(date[0], end='/')
  print(date[1], end='/')
  print(date[2])
else:
  print(birth_date)
print('Address: '+address)
print('')

#### Question3 ####
num = int(input('enter a number: '))
str_num = str(num)
count = 0
while num>1:
  num/=10
  count+=1
print(str_num, ' has ', count, ' digits' )
print('')

#### QUESTION4 ####
grade = int(input('enter your grade: '))
print(grade, end='')
print(' is equivalent to ', end='')
if grade >=90:
  if grade >=97:
    print('an A+')
  elif grade >=94:
    print('an A')
  else:
    print('an A-')
elif grade >=80:
  if grade >=87:
    print('a B+')
  elif grade >=84:
    print('a B')
  else:
    print('a B-')
elif grade >=70:
  if grade >=77:
    print('a C+')
  elif grade >=74:
    print('a C')
  else:
    print('a C-')
elif grade >=60:
  if grade >=67:
    print('a D+')
  elif grade >=64:
    print('a D')
  else:
    print('a D-')
else:
  print('an F')
print('')

#### QUESTION5 ####
n = int(input('enter a number: '))
for i in range(1,n+1):
  print('*'*i)
for i in range(n-1,0,-1):
  print('*'*i)
print('')

#### QUESTION6 ####
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
check = num2-num1
even = []
if check>0:
  low=num1
  high=num2
else:
  low=num2
  high=num1
for i in range(low,high+1):
  if i%2==0:
    even.append(i)
print(even)
  