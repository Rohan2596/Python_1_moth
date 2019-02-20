import numpy as np 
import datetime 
import math
def anagram(s1,s2):
	s1=list(s1)
	s2=list(s2)
	if len(s1)==(len(s2)):
		s1=set(s1)
		s2=set(s2)
		s3=set()
		if s1^s2==s3:
			print("Anagram")
		else:
			print("not an anagram")
	else:
		print("String are ****NOT*** Anagram")

def primerange(num):
	newarr=[]
	for num in range(0,num+1):
		if num>1:
			for i in range(2,num):
				if num%i==0:
					break
			else:
				#print(num,' ',sep=',',end='')
				newarr.append(num)
	print(newarr)
def primeanagram(num):
	cnt=0
	newarr=[]
	new=[]
	for num in range(0,num+1):
		if num>1:
			for i in range(2,num):
				if num%i==0:
					break
			else:
				#print(num,' ',sep=',',end='')
				newarr.append(num)
	print(newarr)
	for i in range(0,len(newarr)):
		for j in range(i+1,len(newarr)):
			newarr[i]=str(newarr[i])
			newarr[j]=str(newarr[j])
			if len(newarr[i])== len(newarr[j]):
				s1=set(newarr[i])
				s2=set(newarr[j])
				s3=set()
				if s1^s2==s3:
					print(" ******Anagram******")
					cnt+=1
					new.append(s1)
					new.append(s2)
					print("Anagram:-",new)
					print("total count",cnt)
				else:
					print("not an anagram")

			else:
				print("String are ****NOT*** Anagram")
	for i in range(0,len(newarr)):
		newarr[i]=str(newarr[i])
		newarr[j]=newarr[::-1]
		if len(newarr[i])==len(newarr[j]):
			if newarr[i]==newarr[j]:
				print("palindrome")
				cnt+=1
				print(cnt)
			else:
				print()
		else:
			print()
def insertionsort(alist):
	# alist=alist.split(" ")
	for i in range(0,len(alist)):
		print(len(alist))
		current=alist[i]
		while i>0 and alist[i-1]>current:
			alist[i]=alist[i-1]
			i=i-1
			alist[i]=current
	print (alist)

def bubblesort(alist):
	# alist=alist.split(" ")

	for i in range(1,len(alist)):
		
		for j in range(i):
			if alist[j]>alist[j+1]:
				temp=alist[j]
				alist[j]=alist[j+1]
				alist[j+1]=temp
	print(alist)
	print(len(alist))

def convert(string):
	li=list(string.split(" "))
	return li

def binaryserach(alist,key,length):
	start=0
	end=length-1
	mid=0
	print(start,end)
	while start<=end:
		mid=end//2
		if key == (alist[mid]):
			print("\nEntered number is present at position",key,mid)
			return -1
		elif key<alist[mid]:
			end=mid-1
		elif key > alist[mid]:
			start=mid +1
	print("\n Element not found")
	

def dayofweek(m,d,y):
	# m=int(input("Enter the month :"))
	# d=int(input("Enter the date :"))
	# y=int(input("Enter the year :"))
	today=datetime.datetime(y,m,d)
	Day=today.weekday()
	print(Day)
	yo=y-(14-m)/12
	x=yo +(yo/4)-(yo/100)+(yo/400)
	print(yo,x)
	mo= m+12*((14-m)/12)-2
	do=(d+x+(31*mo/12))%7
	print(x,mo,do)
	d1=math.floor(do)
	print(d1)
	if Day==0:
		print("Monday")
	elif Day ==1:
		print("Tuesday")
	elif Day ==2:
		print("Wednesday")
	elif Day ==3:
		print("Thursday")
	elif Day ==4:
		print("Friday")
	elif Day ==5:
		print("Saturday")
	else:
		print("Sunday")

	if d1==1:
		print("Monday")
	elif d1 ==2:
		print("Tuesday")
	elif d1 ==3:
		print("Wednesday")
	elif d1 ==4:
		print("Thursday")
	elif d1 ==5:
		print("Friday")
	elif d1 ==6 :
		print("Saturday")
	else:
		print("Sunday")

def tempCon(c,f):
	a=c*9/5 +32
	print("Celsius to fahrenheit: ",a)
	b = (f-32)*5/9
	print("fahrenheit to Celsius: ",b)

def monpay(Y,R,P):
	r=R/(12*100)
	n=Y*12
	p1=P*r
	p2=math.pow(1/(1+r),n)
	p3=1-p2
	print("Enter the number of years in months :- ",n)
	print("Enter the rate of interset ")
	print("Payment to be paid monthly:",p1/p3)
	print("Total amount  to be paid back all together",(p1/p3)*n)
	print(n,r)
	print(p1,p2)

def dectobinary(n):
	binaryarr=[0]*8
	i=0
	while n>0:
		binaryarr[i]=n%2 
		n=int(n/2)
		i+=1
	for j in range(7,-1,-1):
		print(binaryarr[j],end=" ")
	return binaryarr
def swap(dec):
	j=7
	for i in range(3,-1,-1):
		temp=dec[i]
		dec[i]=dec[j]
		dec[j]=temp
		j-=1
	print()
	for j in range(7,-1,-1):
		print(dec[j],end=" ")
	
def bintodec(binaryarr):
	for i in range(0,len(binaryarr)):
		if binaryarr[i]==1:
			k=math.pow(2,i)
			print(k)
		elif binaryarr[i]==0:
			print()

def mergesort(alist):
	if len(alist)>1:
		mid=len(alist)//2
		lefthalf=alist[:mid]
		righthalf=alist[mid:]
		mergesort(lefthalf)
		mergesort(righthalf)
		print(mid)
		print(lefthalf)
		print(righthalf)
		for i in range(1,len(lefthalf)):
			for j in range(i):
				if lefthalf[j]> lefthalf[j+1]:
					temp=lefthalf[j]
					lefthalf[j]=lefthalf[j+1]
					lefthalf[j+1]=temp
					i+=1
		print(lefthalf)   
		for i  in range(1,len(righthalf)):
			for j in range(i):
				if righthalf[j] > righthalf[j+1]:
					temp=righthalf[j]
					righthalf[j]=righthalf[j+1]
					righthalf[j+1]=temp
		print(righthalf)
		for i in range(1,len(alist)):
			for j in range(0,i):
				if alist[j]>alist[j+1]:
					temp=alist[j]
					alist[j]=alist[j+1]
					alist[j+1]=temp
	print(alist)

def vendmac(notes):
	print("Amount Enterds into vebding machine",notes)
	no=[]
	n1=[1000,500,200,100,50,20,10,5,2,1]
	i=-1
	while notes>=0:
		if i<len(n1)-1:
			i+=1
		if notes>= n1[i]:
			notes=notes-n1[i]
			print(n1[i])
			i=-1

