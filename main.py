from os import system, name 
from datetime import datetime
import hashlib

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

def banner():
    print("                 _       ___                     ")
    print("  /\  /\__ _ ___| |__   / _ \_   _  ___  ___ ___ ")
    print(" / /_/ / _` / __| '_ \ / /_\/ | | |/ _ \/ __/ __|")
    print("/ __  / (_| \__ \ | | / /_\\| |_| |  __/\__ \__ \\")
    print("\/ /_/ \__,_|___/_| |_\____/ \__,_|\___||___/___/")
    print("twitter.com/rootaura")

def strtohash(htype,string):
    if htype == "1":
        return (hashlib.md5(string.encode('utf-8')).hexdigest())
    elif htype == "2":
        return (hashlib.sha1(string.encode('utf-8')).hexdigest())

clear()
banner()
print("1) MD5")
print("2) SHA1")
hashtype = input("Please Select Hash Type : ")
hashstr = input("Please Enter Hash : ")
clear()
banner()
w1 = input("Word 1 : ")
w2 = input("Word 2 : ")
clear()
banner()
wordlist = []
prefixlist = ["!",".","-","_","A","123","321","1234","12345","123456","321","1903","1907","1905","1967"]
w1 = str(w1)
w2 = str(w2)
dt = datetime.now()
yearoftoday = dt.strftime("%Y")
for i in range(1970,int(yearoftoday)):
    wlist = []
    wlist.append(w1)
    wlist.append(w2)
    wlist.append(str.capitalize(w1))
    wlist.append(str.capitalize(w2))
    wlist.append(str(i))
    for pre in prefixlist:
        wlist.append(pre)
    for ww1 in wlist:
        for ww2 in wlist:
            for ww3 in wlist:
                for ww4 in wlist:
                    wordlist.append(ww1 + ww2 + ww3 + ww4)
                    wordlist.append(ww1 + ww2 + ww3)
                    wordlist.append(ww1 + ww2)
clear()
banner() 
found = False
print("Wordlist created with " + str(len(wordlist)) + " words")
tested = 0
for word in wordlist:
    tested = tested +1
    if strtohash(hashtype,word) == hashstr:
        if found == False:
            print("Found! (" + word + ")")
            found = True
            break
if found == False:
    print("Not Found!")
print("Tested " + str(tested) + " Words.")