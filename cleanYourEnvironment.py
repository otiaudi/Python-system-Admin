import os

#remove dependencies that were installed with the packages using autoremove
#clean obsolete deb- packages using autoclean

def clean_environment(): 
    os.system("sudo apt-get autoremove") 
    os.system("sudo apt-get autoclean")



clean_environment()