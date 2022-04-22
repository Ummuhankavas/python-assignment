## Coding Challenge -1 : Palindrome

##Purpose of the this coding challenge is to solve a control flow statements issue.



### Problem Statement
  
#- Write a function/functions that checks whether the sentence you get from the user is a **palindrome**. (Do not consider punctuation and special characters. Only consider "***alphanumeric***" characters.)


#```bash
#input : "ey edip adana'da, pide ye!"

#output : "ey edip adana'da, pide ye!" is a palindrome

#input : "Was it a car or a cat I saw?"

#output : "Was it a car or a cat I saw?" is a palindrome
#```

def is_palindrome(string) :
      # backwords = string[::-1]
  return string[::-1].casefold() == string.casefold()

def palindrome_sentence(sentence) :
  string=""
  for char in sentence :
    if char.isalnum():
      string += char
  print(string)
  return is_palindrome(string)

word = input("Please enter a words to check : ")
if palindrome_sentence(word) :
  print("'{}' is a palindrome".format(word))
else :
  print("'{}' is not a palindrome".format(word))

