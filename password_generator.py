import string
import random

if __name__  == "__main__":
    s1= string.ascii_uppercase
    #print(s1)
    s2= string.ascii_lowercase
    #print(s2)
    s3= string.digits
   # print(s3)
    s4= string.punctuation
   # print(s4)
   
  #Asking the user to enter the password length 
    plen = int(input("Enter the password length: \n")) 
    password = []

    password.extend(list(s1))
    password.extend(list(s2))
    password.extend(list(s3))
    password.extend(list(s4))
    #print(s)

    random.shuffle(password) #shuffles the password so it's not predictable.
    print("".join(password[0:plen]))








