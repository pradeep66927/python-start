## NORMAL WAY TO DO SUM

# a=int(input("enter first no: "))
# b=int(input("enter second no: "))
# c=a+b
# print("addition of a and b= ",c)

## ******** BY USING FUNCTION ************

# def add():
# 	a=int(input("enter first no: "))
# 	b=int(input("enter second no: "))
# 	c=a+b
# 	print("addition of a and b = ",c)
# add()

# this is not a good way to write function code

###########################################################
# def add(a,b):
# 	c=a+b
# 	print("addition of a and b = ",c)
# t=int(input("enter first no : "))
# z=int(input("enter second no :"))
# add(t,z)

##******** or or or or or or or or or or or ***************** 

# def add(a,b):
# 	c=a+b
# 	print("addition of a and b = ",c)
# add(10,34)
# add(0.5,7.6)

####################################################################
           ## NORMAL WAY
# n=int(input("enter your no : "))
# count=0
# for i in range (1,n+1):
# 	if n%i==0:
# 		count+=1
# if count==2:
# 	print("prime number")
# else:
# 	print("composite number")
	
# ************### by using function *********

# def prime(n):
# 	count=0
# 	for i in range (1,n+1):
# 		if n%i==0:
# 			count+=1
# 	if count==2:
# 		print("prime number")
# 	else:
# 		print("composite number")
# p=int(input("enter your no : "))
# prime(p)	

################################################################

# def d(a,b):
# 	if a>b:
# 		print(a)
# 	elif a==b:
# 		print(a)
# 	else:
# 		print(b)

# print(d(10,20))

# ## output
# # 20
# # NONE

# def d(a,b):
# 	if a>b:
# 		return(a)
# 	elif a==b:
# 		return(a)
# 	else:
# 		return(b)

# print(d(10,20))

## POSITIONAL ARGUMENT #################

# def d(a,b):
# 	if a>b:
# 		print(a)
# 	elif a==b:
# 		print(a)
# 	else:
# 		print(b)

# d(10,20)

# ## keyword/named ARGUMENT #################

# def d(a,b,c):
# 	if a>b:
# 		print(a)
# 	elif a==b:
# 		print(a)
# 	else:
# 		print(b)

# d(c=10,a=20,b=12)

## DEFAULT argument  ##############################################

# def d(a,b=5):
# 	print("a=",a, "b=",b)
# d(2,10)

## if b=5 assiged above than when we call function and put in place
# of "a" somthing and place of "b" somthing than if a takes that value and b 
# also take value from we call but if call d(2) like this than b automatically
# set its value as above assign(b=5) defaultly


# def d(a,b=5,c=4):
# 	print("a=",a, "b=",b,"c=",c)
# d(2,10,12)

## 2nd rule ## once we set a default value after that every parameter will be like 
## default not as variable like d(a,b=30,c) cant write like this it will shows error


###############################################################################
# find the some of the list element using function with argument

# def add(a,size):
# 	sum=0
# 	for i in range(size):
# 		sum=sum+a[i]
# 	print('sum=',sum)

# #---main
# size=int(input("ener the size of the element :"))
# a=[]
# for i in range(size):
# 	val=int(input("enter the value :"))
# 	a.append(val)
# add(a,size)

######### using RETURN ##############################################


# def add(a,size):
# 	sum=0
# 	for i in range(size):
# 		sum=sum+a[i]
# 	return sum

# #---main
# size=int(input("ener the size of the element :"))
# a=[]
# for i in range(size):
# 	val=int(input("enter the value :"))
# 	a.append(val)

# s=add(a,size)
# print("sum=",s)

## 2 RETURN IN ONE IN SINGLE FUNCTION#######

# def add(a,size):
# 	sum=0
# 	for i in range(size):
# 		sum=sum+a[i]
# 	return sum,i

# #---main
# size=int(input("ener the size of the element :"))
# a=[]
# for i in range(size):
# 	val=int(input("enter the value :"))
# 	a.append(val)

# s,i=add(a,size)
# print("sum=",s,"value index=",i)

#######################################################################

# find the max and min of the list using function argument return
# def maxmin(a,size):
# 	for i in range(size):
# 		max=min=a[0]
# 		if a[i]>max:
# 			max=a[i]
# 		if a[i]<min:
# 			min=a[i]
# 	print("max=",max,"min=",min)

# #__main_____
# size=int(input("enter the number:"))
# a=[]
# for i in range (size):
# 	val=int(input("enter value :"))
# 	a.append(val)
# maxmin(a,size)

## using return find output ############################################
# def maxmin(a,size):
# 	for i in range(size):
# 		max=min=a[0]
# 		if a[i]>max:
# 			max=a[i]
# 		if a[i]<min:
# 			min=a[i]
# 	return max,min

# #__main_____
# size=int(input("enter the number:"))
# a=[]
# for i in range (size):
# 	val=int(input("enter value :"))
# 	a.append(val)
# p,k=maxmin(a,size)
# print("max=",p,"min=",k)

#############################################################################

# find the sum of even and product of odd number using function argument
# def sumpro(a,size):
# 	sum=0
# 	pro=1
# 	for i in range(size):
		
# 		if a[i]%2==0:
# 			sum=sum+a[i]
# 		else:
# 			pro=pro*a[i]
# 	print("sum of even=",sum,"\nprod of odd=",pro)

# #__main_____
# size=int(input("enter the size:"))
# a=[]
# for i in range(size):
# 	val=int(input("entetr value:"))
# 	a.append(val)
# sumpro(a,size)

#### using return ###################################################

# def sumpro(a,size):
# 	sum=0
# 	pro=1
# 	for i in range(size):
		
# 		if a[i]%2==0:
# 			sum=sum+a[i]
# 		else:
# 			pro=pro*a[i]
# 	return sum,pro

# #__main_____
# size=int(input("enter the size:"))
# a=[]
# for i in range(size):
# 	val=int(input("entetr value:"))
# 	a.append(val)
# a,b=sumpro(a,size)
# print("sum of even=",a,"produt of odd=",b)

#################################################################
################## VARIABLE SCOPE ##############################

#GLOBAL VARIABLE
#LOCAL VARIABLE

# def add():
# 	z=a+b
# 	print("additon=",z)

# #__main_____
# a=int(input("enter first no:"))
# b=int(input("enter second no:"))
# add()