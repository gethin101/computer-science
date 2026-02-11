
password_length = False
numbers = False
character_check = False

from playsound import playsound
weak_audio = 

character_data = ["!","£","$","%","^","&","*","(",")","[","]",",",".","/","~","#"]
numbers_data = ["1","2","3","4","5","6","7","8","9","0"]
letters_data = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


print()
password = str(input("Enter password to check strength..  "))



strength = 0
pass_strength = ""



#-------------- length -----------------

if len(password) >= 8:
    password_length = True
    strength += 1


elif len(password) < 8:
    password_length = False


#-------------- letters -----------------
    

if any(char in letters_data for char in password):
    letters = True
    strength += 1

elif not any(char in letters_data for char in password):
    letters = False


#------------- numbers -----------------
    

if any(char in numbers_data for char in password):
    numbers_check = True
    strength += 1

elif not any(char in numbers_data for char in password):
    numbers_check = False


#------------ characters ---------------


if any(char in character_data for char in password):
    character_check = True
    strength += 1

elif not any(char in character_data for char in password):
    character_check = False

#--------------------------------------



#def check_strength():

if strength == 4:
    pass_strength = "Strong"


elif strength == 3:
    pass_strength = "Medium"

else:
    pass_strength = "Strong"


#check_strength()
    

#---------------------------------------




print()
print(f"Strength: {strength}")
print()
print(f"Length check:    {password_length}")
print(f"Letters check:   {letters}")
print(f"Numbers check:   {numbers_check}")
print(f"Character check: {character_check}")
print()
print()
print(f"You password is: {pass_strength}")
print()



print("------------------------------")
print("Suggestions for improvement:")

if not password_length:
    print(f"- Add more length (min 8)")

if not character_check:
    print(f"- Add more special characters")

if not numbers_check:
    print(f"- Add more numbers")


#if not letters:
    #improvement_4 = "letters"
    #print(f"- Add more {improvement_4}")
print("------------------------------")


print()
quit("Closing program... ")










