# !!! Instructions to help you navigate my code !!!
# The code is seprated to three sections from bottom to top:
# 1. Main & Menu function
# 2. Menu Options functions
# 3. Helper functions 
# Any code inspired (!!! not copied !!!) by external resources is referenced at the end of every function
# Every function ending is donoted by #end function

########## 3. Helper Functions ##########

def createDictionary(file): #O(N) N being the number of entries in readlines list
  converted_dict = {}
  # opening and reading text file content:
  with open(file) as content:
    #iterate over readlines() list:
    for pair in content.readlines():
      # separate key-value pair with .split(), store in list
      entry = pair.split(":")
      # key is list item at index0 and value at index1
      converted_dict[entry[0]] = entry[1].replace("\n","")
  return converted_dict
  # readlines() inspired from:
  # https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
# end function

def pickRandomKey(words_dict): #O(1) since we are accessing a list item by a random number
  import random
  # unpack dictionary keys with *, pick an element with random:
  choice = random.choice([*words_dict])
  return choice, words_dict[choice]
  # unpacking and random inspired from:
  # https://www.geeksforgeeks.org/random-numbers-in-python/
  # https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
# end function

def searchDictionary(any_dict, key): #O(N) N being number of keys
  # check if key is in keys list
  if key in any_dict.keys():
    # if found return value
    return any_dict[key]
  # if key not found return False
  return False
# end function
  
def merge(listt, start, mid, end): #O(N), N being the length of the list
  if start == end:
    return

  # first element of the left side
  left = start 
  # first element of the right side
  right = mid+1 

  merge_list=[]
  while left <= mid and right <= end:
  # if element on the left less than right append
    if listt[left] < listt[right]:
      merge_list.append(listt[left])
      left += 1
    else:
      # else append element on the right
      merge_list.append(listt[right])
      right += 1

  #  in case there are elements in left in left side
  while left <= mid:
    merge_list.append(listt[left])
    left += 1
  #  in case there are elements left in right side
  while right <= end:
    merge_list.append(listt[right])
    right += 1

  # the sorted list is the merge_list
  listt[start : end+1] = merge_list
  
# # end function

def mergeSort(listt, start, end): # O(lgN) since we divide list in half every time N being length of list
  # when length of list is 1 stop recursion
  if start >= end:
    return

  mid = (start + end)//2
  mergeSort(listt, start, mid)
  mergeSort(listt, mid+1, end) 
  merge(listt, start, mid, end)
# end function

def hangmanDrawing(num):
  if num == 7: 
    print("\____")
    print(" O  |")
    print("    |")
    print("    |")
    print("    |")
  elif num == 6: 
    print("\____")
    print(" O  |")
    print(" |  |")
    print("    |")
    print("    |")
  elif num == 5: 
    print("\____")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("    |")
  elif num == 4:
    print("\____") 
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("    |")
  elif num == 3: 
    print("\____")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("    |")
  elif num == 2: 
    print("\____")
    print(" O  |")
    print("/|\ |")
    print("/ \ |")
    print("    |")
  elif num == 1: 
    print("\____")
    print(" O  |")
    print("/|\ |")
    print("/ \ |")
    print("   l|")
  elif num == 0: 
    print("\____")
    print(" O  |")
    print("/|\ |")
    print("/ \ |")
    print("l  l|")
# end function

########## 2. Menu Options Functions #########

def saveDictionary(any_dict, file): # O(N) N being the number of keys in the dict
  pairs_list = []
  # iterate over dict, convert key-value to file entry version, append to list
  for key, value in any_dict.items():
    pair = key + ":" + value + "\n"
    pairs_list.append(pair)
    # write list to text file
  with open(file,'w') as file:
    file.writelines(pairs_list)
    # writing to a file inspired from:
    # https://www.geeksforgeeks.org/writing-to-file-in-python/
# end function

def changeWord(words_dict): # O(N) since it has the complexity of function searchDictionary
  word = input("enter word to change:")
  # check for word in dict
  hint = searchDictionary(words_dict, word) 
  # if found, print hint
  if hint:
    print(" word found, it's hint =>",hint)
    # prompt for new hint, update words dict
    new_hint = input("Enter new hint: ")
    words_dict[word] = new_hint
  else:
    print("word not found")
# end function

def removeWord(words_dict): # O(N) => searchDictionary()
  word = input("enter word to remove: ")
  # check if word in dict
  hint = searchDictionary(words_dict,word)
  # if found, reasure if user wants to delete
  if hint:
    option = input("are you sure you want to delete "+word+":"+ hint + " ?[y/n]")
    if option == 'y':
      del words_dict[word]
  else:
    print("word not found")
# end function

def addWord(words_dict): # O(N) => searchDictionary()
  # prompt user for new word
  added_word = input("Enter word to add:")
  # check if word is already in dict
  hint = searchDictionary(words_dict, added_word)
  if hint:
    print("word is already in dictionary!")
  else:
    # if not found prompt for hint and add word to dict
    hint = input("Enter hint:")
    words_dict[added_word] = hint
# end function

def listWords(words_dict): # O(NlgN) => mergeSort()
  # get keys list, and sort it
  keys_list = [*words_dict]
  mergeSort(keys_list, 0, len(keys_list)-1)
  # This code was intended to print dictionary version of the sorted words list but question said to print words (list)
  # sorted_dict = {}
  # for i in range(len(keys_list)):
  #   key = keys_list[i]
  #   value = words_dict[key]
  #   sorted_dict[key] = value
  
  # check if dictionary is empty
  if not keys_list:
    print("The dictionary is empty. Please add to dictionary using option 3")
  else:
    print(keys_list)
# end function

def playHangman(words_dict, old_score): # O(N**2) N being length of word
  mode = input("Enter game mode [easy/hard]:")
  # if user played before print their total score
  if old_score:
    print("-"*30)
    print("\t\tSCORE", old_score)
    print("-"*30)
  # get a random word
  word , hint = pickRandomKey(words_dict)
  # initialize variables for tracking and mask word
  attempts = 8
  guessed = 0
  letters_entered = []
  score = 0.0
  dashes = "_"*len(word)
  dashed_list = [*dashes]
  # create a list of the unique characters of the word
  char_list =[]
  for ch in word:
    if ch not in char_list:
      char_list.append(ch)
  # make a stoping condition if user guesses word and still has attempts left
  char_number = len(char_list)
  
  # the game begins, print dashed word and hint if easy mode
  if mode == "easy":
    print(dashed_list, hint)
  else:
    print(dashed_list)
  # keep prompting user for a guess, display dashed word, attempts left, and score every time a letter is guessed
  while attempts > 0 and guessed < char_number:
    letter = input("Enter a letter guess: ")
    #if users guess is in word, calculate score
    if letter in word and letter not in letters_entered:
      guessed +=1
      letters_entered.append(letter)
      score = round((guessed/char_number)*100, 1)
      # unmask guessed letter in dashed word
      for i in range(len(word)):
        if word[i] == letter:
          dashed_list[i] = letter
    # if users chooses same letter prevent him
    elif letter in letters_entered:
      print("you already chose", letter)
    else:
      # if users didn't guess decrement attempts left
      letters_entered.append(letter)
      attempts -= 1
      hangmanDrawing(attempts)
    # print attempts, score, and dashed list either way
    print("You still have", attempts, "attempts left","\t\t\tScore:",score)
    print(dashed_list)
  # when a round of the game ends, print achieved score 
  print("your score for this game is", score)
  # ask user if they want to play another round
  choice = input("\nplay again? [y/n]:")
  # if yes, function is called again in main
  return score, choice

########## 1. Main & Menu Function ##########

def displayMenu():
  print("\n")
  print("1.Play Hangman\n" + "2.List Words in Dictionary\n" + "3.Add Word to Dictionary\n" + "4.Remove Word from Dictionary\n" + "5.Change Word Hint\n" + "6.Exit")
# end function

def main():
  #Prompt user for their name and display menu
  name = input("Enter your name: ")
  print("\n************ Welcome", name,"************\n"+
        "Please choose one of the options below:")

  displayMenu()

  # Initialize global variables needed:
  words_dict = createDictionary("dictionary.txt")
  users_dict = createDictionary("users.txt")
  #Check users option and run corresponding function
  option = eval(input())
  while option != 6:
    
    if option == 1:
      # check if user played before
      old_score = float(searchDictionary(users_dict, name))
      if not old_score:
        old_score = 0.0
      # run game, get score and user's choice if they want to play again
      score, choice = playHangman(words_dict, old_score)
      while choice == 'y':
        # add score from previous round to old score
        old_score += score
        score, choice = playHangman(words_dict, old_score)
      # update the final score value to last rounds score and old score
      score += old_score
      users_dict[name] = str(score)
      # save changes to file
      saveDictionary(users_dict, "users.txt")
      
    elif option == 2:
      listWords(words_dict)
    elif option == 3:
      addWord(words_dict)
    elif option == 4:
      removeWord(words_dict)
    elif option == 5:
      changeWord(words_dict)
    else:
      print("Invalid Input please choose again")

    displayMenu()
    option = eval(input())
    
  save = input("do you want to save changes to dictionary? [y/n]: ")
  if save == 'y':
    saveDictionary(words_dict, "dictionary.txt")
  print("You Exited ..")
# end function
# execute main
main()