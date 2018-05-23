 #!/usr/bin/env python3

import shutil
import os
import sys
import argparse
import subprocess


b_cli="bitcoin-cli -datadir=$HOME/bitcoindir "
exc_cli="$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 "
bob_cli="$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 "
miner_cli="$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir3 "

b_dae="bitcoind -datadir=$HOME/bitcoindir "
exc_dae="$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1 "
bob_dae="$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2 "
miner_dae="$HOME/elements/src/elementsd -datadir=$HOME/elementsdir3 "

def envSetup():
	print("[Info] Setting up environment...")
	subprocess.call("rm -r ~/bitcoindir;rm -r ~/elementsdir1;rm -r ~/elementsdir2;rm -r ~/elementsdir3", shell=True)  
	subprocess.call("mkdir ~/bitcoindir ; mkdir ~/elementsdir1 ; mkdir ~/elementsdir2 ; mkdir ~/elementsdir3", shell=True)  
	shutil.copyfile("/home/olaya/elements/contrib/assets_tutorial/bitcoin.conf", "/home/olaya/bitcoindir/bitcoin.conf")
	shutil.copyfile("/home/olaya/elements/contrib/assets_tutorial/elements1.conf", "/home/olaya/elementsdir1/elements.conf")
	shutil.copyfile("/home/olaya/elements/contrib/assets_tutorial/elements2.conf", "/home/olaya/elementsdir2/elements.conf")
	shutil.copyfile("/home/olaya/elements/contrib/assets_tutorial/elements3.conf", "/home/olaya/elementsdir3/elements.conf")



# Initializes bitcoin and elements daemons (e1, e2)
def startd():
	envSetup()
	print("[Info] Starting daemon services...")
	subprocess.call(b_dae, shell=True)  
	subprocess.call(exc_dae, shell=True)  
	subprocess.call(bob_dae, shell=True)  
	subprocess.call(miner_dae, shell=True)  
	return 1

# Stops bitcoin and elements daemons (e1, e2)
def stopd():	
	print("[Info] Stopping daemon services...")
	subprocess.call(b_cli + "stop", shell=True)  
	subprocess.call(exc_cli + "stop", shell=True)  
	subprocess.call(bob_cli + "stop", shell=True)  
	subprocess.call(miner_cli + "stop", shell=True)
	return 1  

def validClient(args):
	print("*******validClient*******")

	if(args == "exc_cli"):
		return exc_cli
	elif(args == "bob_cli"):
		print("returning,", bob_cli)
		return "" + bob_cli
	elif(args == "miner_cli"):
		return miner_cli
	elif(args == "b_cli"):
		return b_cli
	else:
		return 0

#NEED TO FIX RETURN STATEMENT FROM THIS FUNCTION...


def validCmd(args):
	print("validCmd:" + args)
	return 1

if __name__ == "__main__":
	# parser = argparse.ArgumentParser()
	# parser.add_argument('block_time', type=int, help='Block generation time interval')
	next_uinput = 1
	dservices = 0
	while(next_uinput):
		uinput = input("\nEnter command: ")
		if(uinput == "startd"):
			dservices = startd()
		elif(uinput == "stopd"):
			dservices = stopd()
		elif(uinput == "exit"):
			if(dservices == 1):
				dservices = stopd()
			next_uinput = 0
		else:
			args = uinput.split()
			if(dservices == 0):
				dservices = startd()
			if(validClient(args[0])):
				cmd = validCmd(args[1])
				print()
				print("[MAIN] cmd:", cmd)
				print(cmd)
				if(cmd):
					print("made it inside")
					subprocess.call(str(cmd) + " " + args[1], shell=True)  
				else:
					print("[ERROR] Command not recognized")
			else:
				print("[ERROR] Not a valid input: (" + args[0]+ ") - exc_cli, bob_cli, miner_cli must be given")

#bob-cli getwalletinfo