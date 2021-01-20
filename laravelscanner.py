#!/usr/bin/python
# -*- coding: utf-8 -*
#Scanner LARAVEL
#Youtube : 
# Blog : 
#####################################
import requests, re, urllib2, os, sys, codecs, random           
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time
from zlib import compress, decompress
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)

abang = Fore.RED
ijo = Fore.GREEN
putih = Fore.WHITE
biru = Fore.BLUE
kuning = Fore.YELLOW
mbohopo = Fore.MAGENTA


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
            ╔╗───╔═══╗╔═══╗╔═══╗╔╗──╔╗╔═══╗╔╗───
            ║║───║╔═╗║║╔═╗║║╔═╗║║╚╗╔╝║║╔══╝║║───
            ║║───║║─║║║╚═╝║║║─║║╚╗║║╔╝║╚══╗║║───
            ║║─╔╗║╚═╝║║╔╗╔╝║╚═╝║─║╚╝║─║╔══╝║║─╔╗
            ║╚═╝║║╔═╗║║║║╚╗║╔═╗║─╚╗╔╝─║╚══╗║╚═╝║
            ╚═══╝╚╝─╚╝╚╝╚═╝╚╝─╚╝──╚╝──╚═══╝╚═══╝
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()
start_raw = raw_input("\n\033[91mGive,Me List Dear\033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:
    with open(start_raw, 'r') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
    
try:
    ooo = list((ooo))
except NameError:
    print '\033[31mOpen Your Eyes!'
    sys.exit()
count=0
with open(start_raw,'r')as f:
 for line in f:
    count+=1
print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92mTOTAL WEBLIST=',count


def kcfinder(url):
	try:
		Agent1 = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36'}
		ajg = ['']
		for ajg1 in ajg:
			asu = requests.get(url+'/'+ajg1+'/vendor/phpunit/phpunit/phpunit.xml',headers=Agent1, timeout=15)
			if "PHPUNIT_TESTSUITE" in asu.content:
				print(url+ ijo + '[!] LARAVEL . . .')
				open('laravel.txt', 'a').write(url+'/'+ajg1+'\n')
			else:
				print(url+ abang + '[!] Not LARAVEL . . .')
	except:
		pass

def Main():
    try:
        start = timer()
        pp = Pool(int(crownes))
        pr = pp.map(kcfinder, ooo)
        print('TIME TAKE: ' + str(timer() - start) + ' S')
    except:
        pass


if __name__ == '__main__':
    Main()
    