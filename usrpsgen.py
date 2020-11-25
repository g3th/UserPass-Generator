#!/usr/bin/python3
#secure password generator
from bs4 import BeautifulSoup as bs
from random import randint
import os, requests


os.system("cls")

class password_generator():
    
    def __init__(self):                                 #constructor and
        self.num=randint(0,9)                           #variables
        self.sym="{@}#1!'*-=}["
        self.dig="abcdefghijklmnopqrstuvwxyz"
        
    def gen(self):                                      #generator algorithm                    
        sy=randint(0,11);di=randint(0,25)                                            
        s=self.sym[sy];d=self.dig[di]
        randomize=[self.num,s,d]                 
        r=randint(0,2)
        passgen=randomize[r]
        for i in self.dig:
            if i in str(passgen):
                passgen.upper()
        return passgen

    def lcon(self,l):                                   #list to string                           
        finalpass=""                                
        for i in l:
            finalpass=finalpass+str(i)
        return finalpass


class u_gen():

    def __init__(self):
        suffix=randint(100,999)
        self.user=str(suffix)

    def canned_soup(self):
        url="https://randomword.com/"
        header={'User-Agent':'Firefox 83.0'}
        req=requests.get(url,headers=header)
        soup=bs(req.text,'html.parser')
        return soup

    def word_scraper(self):
        while True:
            w=u_gen.canned_soup(self).find('div',{'id':'random_word'})
            if len(w.text)<7:
                continue
            else:
                break 
        return w.text.capitalize()+self.user

    
while True:                     #user input+validation
    try:
        opt=int(input("How many characters(8 min/20 max)? "))
        if opt<8 or opt>20:
            os.system("cls")
        else:
            break
    except:
        os.system("cls")
        
passw=[]
while len(passw)<opt:                               #eliminate duplicates
    p=password_generator()                          #(list to dict to list)
    #print(p.gen())                                 #before str conversion
    passw.append(p.gen())
    passw=list(dict.fromkeys(passw))                      
                                                        
password=p.lcon(passw)
word=u_gen()
print("\nYour generated username: \n")
print(word.word_scraper())
print("\nYour generated password: \n")
print(password)
print("\nCheers, ears.")
