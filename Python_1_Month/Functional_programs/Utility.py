import random
import math
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

def isprime(num):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				print(num,"is not a prime number")
				print(i,"times",num//i,"is",num)
				break
			else:
				print(num,"is a prime number")
	else:

		print(num,"is not a prime number")
			

