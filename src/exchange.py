 #!/usr/bin/env python3

import shutil
import os
import sys
import argparse
import subprocess
from pathlib import Path
from account import Account

client_dict = {}
dservices = 0 		# daemon services flag 

def envSetup():
	print("[Info] Setting up environment and intializing services")
	home = str(Path.home())
	client_dict["btc"] = "bitcoin-cli -datadir=" + home + "/bitcoindir "
	client_dict["exc"] = "" + home + "/elements/src/elements-cli -datadir=" + home + "/elementsdir1 "
	client_dict["bob"] = "" + home + "/elements/src/elements-cli -datadir=" + home + "/elementsdir2 "
	client_dict["miner"] = "" +home + "/elements/src/elements-cli -datadir=" + home + "/elementsdir3 "
	client_dict["b_dae"] = "bitcoind -datadir=" + home + "/bitcoindir "
	client_dict["exc_dae"] = "" + home + "/elements/src/elementsd -datadir=" + home + "/elementsdir1 "
	client_dict["bob_dae"] = "" + home + "/elements/src/elementsd -datadir=" + home + "/elementsdir2 "
	client_dict["miner_dae"]  = "" + home + "/elements/src/elementsd -datadir=" + home + "/elementsdir3 "

	subprocess.call("rm -r ~/bitcoindir;rm -r ~/elementsdir1;rm -r ~/elementsdir2;rm -r ~/elementsdir3", shell=True)  
	subprocess.call("mkdir ~/bitcoindir ; mkdir ~/elementsdir1 ; mkdir ~/elementsdir2 ; mkdir ~/elementsdir3", shell=True)  
	subprocess.call("cp ~/elements/contrib/assets_tutorial/bitcoin.conf ~/bitcoindir/bitcoin.conf", shell=True)
	subprocess.call("cp ~/elements/contrib/assets_tutorial/elements1.conf ~/elementsdir1/elements.conf", shell=True)
	subprocess.call("cp ~/elements/contrib/assets_tutorial/elements2.conf ~/elementsdir2/elements.conf", shell=True)
	subprocess.call("cp ~/elements/contrib/assets_tutorial/elements3.conf ~/elementsdir3/elements.conf", shell=True)

# Initializes bitcoin and elements daemons (e1, e2)
def startd():
	envSetup()
	subprocess.call(client_dict["b_dae"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
	subprocess.call(client_dict["exc_dae"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
	subprocess.call(client_dict["bob_dae"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
	subprocess.call(client_dict["miner_dae"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
	return 1

# Stops bitcoin and elements daemons (e1, e2)
def stopd():	
	subprocess.call(client_dict["btc"] + "stop", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
	subprocess.call(client_dict["exc"] + "stop", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
	subprocess.call(client_dict["bob"] + "stop", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
	subprocess.call(client_dict["miner"] + "stop", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print("[Info] Daemon services stopped")

	return 0  

def validClient(args):
	if(args == "exc"):
	 	return client_dict["exc"]
	elif(args == "bob"):
		return client_dict["bob"]
	elif(args == "miner"):
		return client_dict["miner"]
	elif(args == "btc"):
		return client_dict["btc"]
	else:
		return 0

# returns - first value specifies if there will be another input requested by user
def parseInput(args):
	global dservices
	print("parseInput - dservices:", dservices )

	if(len(args) == 1):
		if(args[0] == "startd"):
			print("[Info] - Daemon services are running")
			return 1
		elif(args[0] == "exit"):
			print("its exit, dservices:", dservices)
			if(dservices == 1):
				dservices = stopd()
			return 0
		elif(args[0] == "stopd"):
			if(dservices != 0):
				dservices = stopd()
			else:	
				print("[Info] Daemon services are not running")
			return 1
		else:
			print("[ERROR] Invalid command, try again")
			return 1
	else:
		if(dservices == 0):
			print(dservices == 0)
			dservices = startd()
		client = validClient(args[0])
		if(client):
			executeCmd(client, args)

		else:
			print("[ERROR] - Invalid client name given")
		return 1


def executeCmd(client, args):
	# print("[Info] executeCmd - client:", client, " args:", args)	
	cmd = client
	if(args[1] == "getwalletinfo"):
		cmd += "getwalletinfo"	
	else:
		# new_accstart = Account()
		# acc.name = "Daniel"
		print("*********Printing acc***********")
		# print(acc)

	

	print("[Executing]:", cmd)	
	subprocess.call(cmd, shell=True) 
	# p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)


	for line in p.stdout:
		if "bitcoin" in line.decode("utf-8"):
			print(line.decode("utf-8"))
			waka = line.decode("utf-8").split()
			print(float(waka[1])-1.2)
			print(type(float(waka[1])))
	# for line in p.stdout:
	# 	# if "bitcoin" in line:
	# 	print(line)


if __name__ == "__main__":

	next_uinput = 1
	while(next_uinput):
		uinput = input("\nEnter command: ")
		args = uinput.split()
		if(len(args) <= 1):
			next_uinput = parseInput(args)
		if(len(args) > 1):
			next_uinput = parseInput(args)

# bob getwalletinfo