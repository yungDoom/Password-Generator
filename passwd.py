import string
import random
 
length = int(input("Enter password length: "))
 
print('''
Choose character set for password from here : 
         1. Digits/Numbers
         2. Letters
         3. Special Characters
         4. Exit/Leave or see the results
''')
 
charactersetList = ""
 
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
         
    
        charactersetList += string.ascii_letters
    elif(choice == 2):
         
   
        charactersetList += string.digits
    elif(choice == 3):
         
      
        charactersetList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(length):
   
    randomcharacter = random.choice(charactersetList)
     
    password.append(randomcharacter)
 
print("Your random password is " + "".join(password))
