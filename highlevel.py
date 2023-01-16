import pendulum
import os
import sys
import subprocess
import pkg_resources

needed_packages = "pendulum"


class packagecheck:    
    def package_check(): 
        required = {needed_packages}
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = required - installed 

        if missing:
             python = sys.executable
             subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
packagecheck.package_check()

#Intaking file names for naming the files

toplevel = input("Enter which semester you will be in i.e Fall 2023: ")
toplevelname = toplevel + " Semester"
classes = []
done = True
while (done) : 
    newclass = input("Enter Class You are Taking this Semester or Done if done entering classes : ")
    if newclass == "done":
        done = False
    classes.append(newclass)
   
#Making the directories
done = True
path = []
while(done):
    newpath = input(
"""Enter Path to Onedrive Directory one Step at a Time
Type Done if path is full defined""")
    if newpath == "Done":
        done = False
    path.append(newpath)
    print(path)
    pathcommand = 

    
    




        
         




