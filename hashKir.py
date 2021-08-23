#!/usr/bin/env python
#-*- coding: utf-8 -*-
from termcolor import colored
import hashlib
def tryOpen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist,"r")
    except:
        print(colored("[!!] Dosya KOnumu Yanlış.." , "red"))
        quit()

hashGir = input("String Gir: ")
wordlist = input("wordlist KOnumu Girin: ")
tryOpen(wordlist)

for word in pass_file:
    print(colored("[?UĞRAŞIYORUM: "+ word.strip("\n"),"red"))
    enc_word = word.encode("latin-1")
    md5Digest = hashlib.md5(enc_word.strip()).hexdigest()
    if md5Digest == hashGir:
        print(colored(f"[+]Password: {word}" , "green"))
        exit()
print("[!!] Dosyada Şifre Bulunamadı...")