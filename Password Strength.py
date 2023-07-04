import re

password_strength_finder=input("Please write your password.")

a=re.search("[0-9]",password_strength_finder)

if a:
    password_len=len(password_strength_finder)
    print(password_len)

    if password_len>=8:
        print("Your password reaches past our password policy.")
    
    


    else:
        print("Your password is weak try to add atleast 8 characters.")

else:
    print("Your password your password is very weak try adding atleast 1 number in your password.")
  
