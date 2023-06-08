import serial


    
print("this is good things")
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#ser.flush()
x = int(input("hello"))    

while True:
	print("hello")
	if x < 0:
		break
	#if ser.in_waiting > 0:
		#line = ser.readline().decode('utf-8').rstrip()
		#print(line)
