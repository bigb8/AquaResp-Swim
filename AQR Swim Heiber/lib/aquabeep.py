import time,sys
import winsound

tm = int(sys.argv[1])
# tm = 35

time.sleep(tm-30)

winsound.Beep(500,500)
time.sleep(10)
winsound.Beep(550,500)
time.sleep(10)

for some in range(0,10):
	# print some
	winsound.Beep(650,100)	
	time.sleep(1)
	
winsound.Beep(700,1000)