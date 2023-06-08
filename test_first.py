import subprocess


print("This is first testing area")

x = int(input("Enter number : "))

if x == 1 :
    print("Staying")
elif x == 2 : 
    print("Go to the next Module area")
    subprocess.Popen(["kill"])
    
    
    
    subprocess.call("python ex.py", shell=True)
