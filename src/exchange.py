 #!/usr/bin/env python3

import sys
import argparse
import subprocess

b_dae="bitcoind -datadir=$HOME/bitcoindir "
b_cli="bitcoin-cli -datadir=$HOME/bitcoindir "
e1_cli="$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 "
e2_cli="$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 "
e1_dae="$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1 "
e2_dae="$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2 "

# Initializes bitcoin and elements daemons (e1, e2)
def init():
	print("Starting services...")
	return_code = subprocess.call(b_dae, shell=True)  
	return_code = subprocess.call(e1_dae, shell=True)  
	return_code = subprocess.call(e2_dae, shell=True)  

# Stops bitcoin and elements daemons (e1, e2)
def exit():
	print("Stopping services...")
	return_code = subprocess.call(b_cli + "stop", shell=True)  
	return_code = subprocess.call(e1_cli + "stop", shell=True)  
	return_code = subprocess.call(e2_cli + "stop", shell=True)  


if __name__ == "__main__":
	# parser = argparse.ArgumentParser()
	# parser.add_argument('block_time', type=int, help='Block generation time interval')
	next_cmd = 1
	while(next_cmd):
		cmd = input("\nEnter command: ")
		if(cmd == "init"):
			init()
		elif(cmd == "stop"):
			exit()
			next_cmd = 0
		elif(cmd == "e1 getwalletinfo"):
			return_code = subprocess.call(e1_cli + "getwalletinfo", shell=True)  

