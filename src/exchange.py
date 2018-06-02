 #!/usr/bin/env python3

from test_framework.authproxy import AuthServiceProxy, JSONRPCException
from pathlib import Path
from account import Account

import os
import random
import sys
import time
import subprocess
import shutil
from decimal import *
from pdb import set_trace


def loadConfig(filename):
	conf = {}
	with open(filename) as f:
		for line in f:
			if len(line) == 0 or line[0] == "#" or len(line.split("=")) != 2:
				continue
			conf[line.split("=")[0]] = line.split("=")[1].strip()
		conf["filename"] = filename
		return conf;

def startbitcoind(datadir, conf, args=""):
	print("datadir: " + datadir)
	subprocess.call("echo $HOME", shell=True)
	subprocess.call("bitcoind -daemon -datadir=" + datadir + "", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print("waiting for bitcoind......")
	return AuthServiceProxy("http://"+conf["rpcuser"]+":"+conf["rpcpassword"]+"@127.0.0.1:"+conf["rpcport"])





print("[Info] Setting up environment and intializing services")
home = str(Path.home())

subprocess.call("rm -r ~/bitcoindir0; rm -r ~/bitcoindir1", shell=True)  
subprocess.call("mkdir ~/bitcoindir0; mkdir ~/bitcoindir1", shell=True)  

# To figure out how to create wallet.dat from command line

b0_datadir="" + home + "/bitcoindir0"
bconfdir="" + home + "/elements/contrib/assets_tutorial/bitcoin.conf"
shutil.copyfile("" + home + "/elements/contrib/assets_tutorial/bitcoin.conf", b0_datadir+"/bitcoin.conf")

b0conf=loadConfig(bconfdir)
cmd="bitcoind " + b0_datadir
print("before startbitcoind")
b1 = startbitcoind(b0_datadir, b0conf)
print("after startbitcoind")
time.sleep(2)
try:
	b1.getinfo()
	raise AssertionError("This should fail unless working bitcoind can be reached via JSON RPC")
except:
	pass
w=b1.getblockchaininfo()
print(w)

print("Wohooooooo working")


subprocess.call("bitcoin-cli -datadir=" + b0_datadir + " stop", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
