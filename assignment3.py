#### add matrices ####
def promptMatrices(option):
  matrix1 = []
  matrix2 = []
  first_matrix = True
  for i in range(1, 3):
    rows = int(input("Enter number of rows:"))
    cols = int(input("Enter number of columns:"))
    for j in range(1, rows+1):
      row = list(map(int, input("Enter elements of row"+str(j)+" of matrix"+str(i)+": ").split()))
      if first_matrix:
        matrix1.append(row)
      else:
        matrix2.append(row)
    first_matrix = False
    if option==2 and i==1:
      rows1 = rows
      cols1 = cols
    if option==2 and i==2:
      rows2 = rows
      cols2 = cols
      return matrix1, matrix2, rows1, cols1, rows2, cols2
  return matrix1, matrix2, rows, cols

def createDictionary():
  dict = {}
  pairs_list = []
  entries = int(input("Enter number of dictionary entries: "))
  temp = list(input("Enter key and value pairs: \n").split())
  for i in range(entries):
    pairs_list.append(temp[i].split(":"))
    dict[pairs_list[i][0]] = pairs_list[i][1]
  # print(dict)
  return dict

def addMatrices():
  print("Add matrices of EQUAL size")
  matrix1 , matrix2, rows, cols = promptMatrices(1)
  matrix3 = []
  for i in range(rows):
    temp = []
    for j in range(cols):
      sum = matrix1[i][j] + matrix2[i][j]
      temp.append(sum)
    matrix3.append(temp)
  print(matrix3)

def checkRotation():
  matrix1, matrix2, rows1, cols1, rows2, cols2  = promptMatrices(2)
  counter = 0
  if rows1 == cols2 and cols1 == rows2:
    for i in range(rows1):
      for j in range(rows2):
        if matrix1[i][j] == matrix2[j][i]:
          counter +=1
    if counter == rows1*rows2:
      print("True")
      return True
    return False
  else:
    return False

def invertDictionary():
  inverted_dict = {}
  dict = createDictionary()
  for key, value in dict.items():
    if value not in inverted_dict:
      inverted_dict[value]= key
    else:
      temp = inverted_dict[value]
      inverted_dict[value] = [key,temp]
    
  print(inverted_dict)

def matrixToDictionary():
  dict_users = {}
  list_users = []
  total = int(input('Enter number of users: '))
  for i in range(1, total+1):
    first_name = input('first name: ')
    last_name = input('last name: ')
    job_title = input('job title: ')
    attributes = [first_name, last_name, job_title]
    list_users.append(attributes)
    print('user',i+1,':')
  print(list_users)
  for i in range(total):
    id = '000'+ str(i)
    dict_users[id] = list_users[i]
  print(dict_users)

def checkPalindrome():
  stri = ""
  input_str = input("Enter String: ")
  for ch in input_str:
      stri = ch + stri
  if stri == input_str:
    print("True")
    return True
  return False

def searchElement():
  pass
  

def displayMenu():
  print("1.Add Matrices\n" + "2.Check Rotation\n" +
       "3.Invert Dictionary\n" + "4.Convert Matrix to Dictionary\n" + "5.Check Palindrome\n" + "6.Search Element\n" + "7.Exit\n")

def main():
  name = input("Enter your name: ")
  print("Welcome", name)
  displayMenu()
  choice = eval(input("Enter your option: "))
  while choice !=7:
    if choice == 1:
      addMatrices()
    if choice == 2:
      checkRotation()
    if choice == 3:
      invertDictionary()
    if choice == 4:
      matrixToDictionary()
    if choice == 5:
      checkPalindrome()
    if choice == 6:
      searchElement()
    if choice == 7:
      print("exit")
      break
    else:
      print('invalid input')
    displayMenu()
    choice = eval(input("Enter your option: "))
      

main()