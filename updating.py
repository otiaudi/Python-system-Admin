import os
#updating packages

def update_environment(): 
    os.system("sudo apt-get update")        #update the package list for packages
    os.system("sudo apt-get upgrade")       #update the current OS
    os.system("sudo apt-get dist-upgrade")  # download and install updates


update_environment()