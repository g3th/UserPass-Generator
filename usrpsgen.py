#!/usr/bin/python3
#secure password generator
from bs4 import BeautifulSoup as bs
from random import randint
import requests


def clear():
	print("\x1bc")                                        

class password_generator():

	def __init__(self):                                 
		self.num=randint(0,9)                          
		self.sym="{@}#1!'*-=}["
		self.dig="abcdefghijklmnopqrstuvwxyz"
	
	def generate_password(self, p_len):
		passw=[];password='';flag=0
		while len(passw)<p_len:
			sy=randint(0,11);di=randint(0,25)
			s=self.sym[sy];d=self.dig[di]
			randomize=[self.num,s,d]
			r=randint(0,2)
			passgen=randomize[r]
			if flag ==0:
				try:
					if passgen.isalpha():
						passgen = passgen.upper(); flag =1
				except:
					pass	
			passw.append(passgen)
			passw=list(dict.fromkeys(passw))
		for char in passw:
			password=password+str(char)
		return str(password)


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
		clear()
		opt=int(input("How many characters(8 min/20 max)? "))
		if opt<8 or opt>20:
			clear()
		else:
			break
	except:
		clear()
p=password_generator()
passw=[]

passw.append(p.generate_password(opt))
#passw=list(dict.fromkeys(passw))                      
	                                                
password=passw
word=u_gen(); clear()
print("\nYour generated username: \n")
print(word.word_scraper())
print("\nYour generated password: \n")
print(*password)
print("\nCheers, ears.\n")
