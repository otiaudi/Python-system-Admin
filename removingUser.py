import os

#removing a user

def remove_user():
    confirm="N"
    while confirm !="Y":
        username=input("Enter the name of the user to remove:  ")
        print("remove the user:" + username + " " + "? (Y/N)")
        confirm=input().upper()
    os.system("sudo userdel  " + username)
    print("user successfully removed ")
        

remove_user()