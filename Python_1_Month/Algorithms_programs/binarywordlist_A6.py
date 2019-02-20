import AlogoUtility as au 
fo= open("foo.txt","r")
str1=fo.read()
print("read :*********   ",str1)

a2=str(input("Enter the key to find in string:- "))
a3=au.bubblesort(au.convert(str1))
au.convert(a2)
length=int(input("enter the length of string:-"))
au.binaryserach(a3,a2,length)

# au.bubblesort(au.convert(str1))
# a2=str(input("Enter the key to find in string:- "))
# # a2=au.convert(a2)
# fo.close()s