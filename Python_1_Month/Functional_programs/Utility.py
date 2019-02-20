import random
import math
import numpy as np
from itertools import permutations
import datetime
def username(n):
	str1="Hello <<Username>>,How are you?"
	if len(n) >= 3 :
		print("Valid Statement")
		a=str1.replace("<<Username>>",n)
		print(a)
	else:
		print("Invalid statement")
def flipcoin():
	total_heads=0
	total_tails=0
	count=0
	while count<100:
		coin=random.randint(1,2)
		if coin ==1:
			print("heads\n")
			total_heads+=1
			count+=1
		elif coin==2:
			print("tails\n")
			total_tails+=1
			count+=1
	sum1=(total_tails)+(total_heads)
	print("\n Okay,you flipped heads",total_heads,"times")
	print("\nand you flipped tails",total_tails,"times")
	print("Percentage of heads",(total_heads/sum1)*100)
	print("Percentage of tails",(total_tails/sum1)*100)

def leapyear(y):
	a=str(y)
	if len(a)==4:
		print("Valid year")
		if (y%4==0 and y%100!=0 or y%400==0):
			print("Year,It is leap year:-",y)
		else:
			print("Year,It is not an Leap year:-",y)
	else:
		print("Invalid Year")

def pow2(n):
	for i in range(0,n+1):
		p2=math.pow(2,i)
		print("power of 2 raised to ",i,"=",p2)

def harmonic(n):
	sum1=0
	if n==0:
		print("The harmonic value is ZERO")
	else:
		for i in range(1,n+1):
			sum1=sum1+(1/i)
			print(sum1)

def isprime(num1):
	for num  in range(2,num1+1):
		if num > 1:
			for i in range(2,num):
				if (num % i) == 0:
					break
			else:
				print(num,'',sep=',',end=' ')
	
def primefactors(num):
	facto=1
	if num<0:
		print("Prime factors of negative numbers does not exits")
	elif num==0:
		print("Prime Factors of zero is 1 ")
	else:
		for i in range(1,num+1):
			facto=facto*i
		print("\nFactorail of Enter numbers:- ",facto)

def gambler(goal):
	total_money=1
	while total_money<goal:
		if total_money==0:
			break
		n=int(input("Enter the bet Numbers:"))
		n1=random.randint(1,2)
		print(n1)
		if (n==n1):
			print("Gambler Won")
			total_money+=1
			print("Total Money Remaining",total_money)
		else:
			print("Gambler lost")
			total_money-=1
			print("total_money Remaining",total_money)

def couponnumber(n1):
	arr=[]
	i=0
	for i in range(0,n1):
		n=random.randint(1,n1)
		if n not in arr:
			arr.append(n)
			i+=1
	print(arr)
	return arr

def two2darray(m,n):
	Matrix1=np.zeros((m,n))
	print(Matrix1)
	Matrix=[[0 for x in range(m)] for y in range(n)]
	print(Matrix)

def threesum0(n1):
	arr=[]
	count=0
	i=0
	for i in range(0,n1):
		n=random.randint(-n1,n1)
		if n not in arr:
			arr.append(n)
			i+=1
	print(arr)
	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			for k in range(j+1,len(arr)):
				if arr[i]+arr[j]+arr[k]==0:
					print(arr[i],arr[j],arr[k])
					count+=1
	print(count)
	
def  euclidean(x,y):
	a=x*x
	b=y*y
	su=a+b
	sqrt=math.pow(su,0.5)
	print("Euclidean distance between:-",sqrt)

def permutations(a):
	x=list(a)
	
	print(x)
	for i in range(0,len(x)):
		for j in range(1,len(x)):
			for k in range(1,len(x)):
				print(x[i],x[j],x[k])
	# perm=permutations(n1,len(n1))
	# print(perm)
	# for i in list(perm):
	# 	print(i)

def start():
	start=datetime.datetime.now().microsecond
	return start
def stop(start):
	stop=datetime.datetime.now().microsecond
	# return (stop-start)
	print(stop-start)

def quadratic(a,b,c):
	delta=(b*b)-(4*a*c)
	d=abs(delta)
	roots1=(-b + (math.sqrt(abs(delta))))/2*a
	print("Roots1:-",roots1)
	roots2=(-b -(math.sqrt(abs(delta)))) / 2*a
	print("Roots2:-",roots2)

def windchill(t,v):
	w=[]
	w1=[]
	w2=[]
	w3=[]
	w1 =35.74 +0.6215*t
	w2 =0.4275*t - 35.75
	w3 =float(math.pow(v,0.16))
	print(w1,"  ",w2,"  ",w3)
	w= w1 + (w2*w3)
	if ((t <=50) and v<=120 and v>=3):
		print("Valid Year")
		print(float(w))
	else:
		print("InValid Year")

def tictactoe():
	pass




