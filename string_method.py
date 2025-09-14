# s = "kanishka Bhardwaj" #string is immutable
# #name[0] = "R" We can't do this 
# a = len(s) # to count the value of the charater in the string
# print(a)
# print(s.upper()) # use to change make it in capital letters 
# print(s.lower()) # use to change make it in small letters 
# print(s.capitalize())#use to change make it first letter capital letters 
# print(s.title()) # to make first letter of ever word in capital.
#text = "Hello world"
#print(text.strip()) #to remove extra space from the word.
#print(text.lstrip()) # to remove extra space towords left
#print(text.rstrip()) #to remove extra space towords right
# text = "Python is fun"
# print(text.find("is")) # this will find at what value of 'is' on.
# print(text.replace("fun" , "good")) # this will replace all the occurrence from fun to good 
# text = "Apple, Bananas, Pineapple"
# print(text.split(",")) # split function convert string into list.
# print(",".join(['Apple', ' Bananas', ' Pineapple'])) # this ll convert list into string.

text ="Python123"
print(text.isalpha()) # Output: False , and it ll check does it contain only alphabet or not 
print(text.isdigit()) # Output: False , it ll check does it contain only number or not 
print(text.isalnum()) # Output: True , it ll check does it contain  alphabet and number
print(text.isspace()) # Output: Fals , it ll check does it only have white space or not 

