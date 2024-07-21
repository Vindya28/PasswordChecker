import string

# password="qwerty"
password=input("Enter your password:")

upper_case =any( [ 1 if c in string.ascii_uppercase else 0 for c in password])

# [ 1 if c in string.ascii_uppercase else 0 for c in password]  
# this creates a list , where if it is lower_case then it assigns 0 else 1
# 'any' will print true if there presents any upper_case in password else false.
# print(string.ascii_uppercase)

 #prints true for 'helloWorld' and false for 'helloworld'


lower_case =any( [ 1 if c in string.ascii_lowercase else 0 for c in password])
special =any( [ 1 if c in string.punctuation else 0 for c in password])
digits =any( [ 1 if c in string.digits else 0 for c in password])

characters=[upper_case,lower_case,special,digits]

length=len(password)

score=0

with open('common.txt','r') as f:
    common= f.read().splitlines()

if password in common:
    print("Password was found in a common list. Score:0 ")
    exit()


if(length>8):
    score+=1
if(length>12):
    score+=1
if(length>16):
    score+=1
if(length>19):
    score+=1

print(f"Password length is {str(length)}, adding {str(score)} points!")

if sum(characters)>1:
    score+=1
if sum(characters)>2:
    score+=1
if sum(characters)>3:
    score+=1

print(f"Password has {str(sum(characters))}, different character types , adding {str(sum(characters)-1)} points!")



if(score<4):
    print(f"password is quite weak! Score: {str(score)}/7")
elif score ==4:
    print(f"password is OKAY! Score: {str(score)}/7")
elif score>4 and score<6:
    print(f"password is Pretty good! Score: {str(score)}/7")
elif score>6:
    print(f"password is Strong! Score: {str(score)}/7")

