import subprocess


print("This is Second testing area")

x = int(input("Enter number : "))

if x == 1:
    print("Go to the next Module area")
    subprocess.call("python test_second.py")
elif x == 2 :
    print("Staying")
elif x == 3 : 
    print("Go to the next Module area")
    subprocess.call("python test_third.py")
    