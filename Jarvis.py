import subprocess
import time


def GoFlow():
    processs = subprocess.Popen("./Bash_Scripts/Go1.sh")
    print(processs.pid)
    print("Go tutorial opened")
    time.sleep(1)
    processs = subprocess.Popen("./Bash_Scripts/Go2.sh")
    print(processs.pid)
    print("Go Code opened")
    time.sleep(1)
    processs = subprocess.Popen("./Bash_Scripts/LC4.sh")
    print(processs.pid)
    print("Github opened")


def LeetCodeWorkFlow():
    process = subprocess.Popen("./Bash_Scripts/LC1.sh") #popen starts process and returns controll to python program
    print(process.pid)
    print("LeetCode opened")
    time.sleep(1)
    process = subprocess.Popen("./Bash_Scripts/LC2.sh")
    print(process.pid)
    print("Portfolio Opened and ran")
    time.sleep(1)
    process = subprocess.Popen("./Bash_Scripts/LC3.sh")
    print(process.pid)
    print("Portfolio opened on browser")
    
    time.sleep(1)
    
    process = subprocess.Popen("./Bash_Scripts/LC4.sh")
    print(process.pid)
    print("Github opened on browser")


def DropMyNeedle():
    process = subprocess.Popen("./Bash_Scripts/Songs.sh")
    print(process.pid)
    print("DropMyNeedle opened")

print("Current Workflows: \n1) LeetCode Workflow\n2) DropMyNeedle\n3) GoFlow") 
userinp = int(input("Enter the task you want to perform: "))
while (userinp != 0):
    if userinp == 1:
        LeetCodeWorkFlow()
    elif userinp == 2:
        DropMyNeedle()
    elif userinp == 3:
        GoFlow()
    else:
        print("Invalid Input")
    userinp = input("Enter the task you want to perform: ")
