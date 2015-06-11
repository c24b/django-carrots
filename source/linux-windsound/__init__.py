import subprocess as sp

#sp.call(["modprobe", "pcspkr"])
#print ("Activating the alert")

class Windsound(object):
		
		
	def Beep(self, freq, time):
		args = ["beep", "-f", str(freq), "-l", str(time)]
		sp.call(args)
		time.sleep(30)
		return

#windsound = Windsound()
#windsoudn.beep(200, 100)
windsound = Windsound()
