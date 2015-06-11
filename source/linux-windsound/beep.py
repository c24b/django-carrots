"""
.. beep.py
Implementations of beeps.
"""
from subprocess import *
import subprocess as sp
import time	


def beep(freq=1000, time=1, block=False):
    """ Beep through the computer's speaker, with frequency *freq*, for the
    duration of *time* seconds. If *block*, do it via a blocking process;
    otherwise do it via a non-blocking process. """
    miliseconds = int(time * 1000)
    command = sp.call if block else sp.Popen
    args = ["beep", "-f", str(freq), "-l", str(miliseconds)]
    command(args)
    time.sleep(3)
    return


def beep_seq(freqs, times):
    """ Beep a sequence of frequency-time pairs; block while doing that. """
    [beep(freq=f, time=t, block=True) for f, t in zip(freqs, times)]


def sirene(low=100, high=2000, time=1, block=True):
    """ Make a sirene-like sequence of beeps. """
    parts = 20
    part = 1.0 * (high - low) / (parts - 1)
    part_time = 1.0 * time / (2 * parts)
    up_seq = [low + n*part for n in xrange(parts)]
    down_seq = [high - n*part for n in xrange(parts)][1:]
    freqs = up_seq + down_seq
    beep_seq(freqs=freqs, times=[part_time]*len(freqs))
    
def sos():
	args = ["beep", "-f", str(250), "-l", str(300)]
	sp.call(args)
	time.sleep(3)
	args = ["beep", "-f", str(150), "-l", str(6000)]
	sp.call(args)
	
#sos()



class Winsoud(object):
	def __init__(self):
		sp.call(["sudo", "modprobe", "pcspkr"])
		sp.call(args)
		print "Activating the alert"
		
	def Beep(self, freq, time):
		args = ["beep", "-f", str(freq), "-l", str(time)]
		sp.call(args)
		return time.sleep(3)
	
	
#~ if __name__ == "__main__":
	#~ windsound = Windsound()
#~ if __name__ == "__init__":
	#~ windsound = Windsound()
