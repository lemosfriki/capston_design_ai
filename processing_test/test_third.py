import subprocess


print("This is Third testing area")

x = int(input("Enter number : "))

if x == 1:
    print("Go to the next Module area")
    subprocess.call("python test_second.py")
elif x == 0 : 
    print("Go to the init Module area")
    subprocess.call("python run.py")