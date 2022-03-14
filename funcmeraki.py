##functions-question1

# def ask_questions():
# 	print("who is the the founder of facebook?")
# 	print(" - Mark Zuckerberg\n# - Bill Gates\n# - Steve Jobs\n# - Larry Page")
#ask_questions()

# ask_questions()
# ask_questions()
# ask_questions()
# ask_questions()
# ask_questions()

## called function  100 time using loop 

# def ask_questions():
# 	print("who is the the founder of facebook?")
# 	print(" - Mark Zuckerberg\n# - Bill Gates\n# - Steve Jobs\n# - Larry Page")
#for i in range(101):
# i=0
# while i<=100:
# 	ask_questions()
# 	i+=1

###################################################################################
## questions-1

# numbers = [3, 5, 7, 34, 2, 89, 2, 5]

# print("maximum number in list=",max(numbers))

## ques-2

# numbers = [1, 2, 3, 4, 5]
# print("sum of numbers=",sum(numbers))

# ## quesn-3
# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# unorder_list.sort()
# print("ordered list =",unorder_list)

## questions-4
# list = [8, 6, 4, 8, 4, 50, 2, 7]

# print("minimum number in list=",min(numbers))

# ## questions-5
# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# reverse_list.reverse()
# print("reverse of list",reverse_list)

################################################################

## DEBUG

## que-1  " : "colon  is missing
## que-2  "def" spelling is wrong like daf
## que-3  "full indentation is missing" in less indentation was there

# isEven()

# def isEven():
# 	if(12%2==0):
# 		print("Even Number")
# 	else:
# 		print("Old Number")
# isEven()

#############################################################################

## Multiple Function Arguments

# def say_hello_language(name, language):
#  if language == "hindi":
#   print("Namaste ", name)
#   print("Aap kaise ho?")
#  elif language == "punjabi":
#   print("Sat sri akaal ", name)
#   print("Tuhada ki haal hai?")
#  else:
#   print("Hello ", name)
#   print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")

##################################################################################

# def say_hello_people(name_x, name_y, name_z, name_a):
# 	print("Namaste ", name_x) # hindi mein

# 	print("Alah hafiz ", name_y) # urdu mein

# 	print("Bonjour ", name_z) # french mein

# 	print("Hello ", name_a) # english mein

# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")

###########################################################################

## Python Arbitrary Arguments

#Arbitrary arguments hum tab use karte hai jab hume pata nahi hota
#hai ki hume kitne no. of arguments function mai dene hai. Hum arbitrary
#arguments ke sath function of define karne ke liye parameter se pehle ( * ) 
#ka use karte hai jai ki neeche dikhaya gaya hai.

# def icecream(*flavours):
# 	for flavour in flavours:
# 		print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry")

###########################################################################3
##Default parameter value

# Default parameter value se yaha humara ye matlab hai ki hum function ko define karte time kisi
# parameter ko value assign kar dete hai taaki hum function ko bina kisi argument ke call kare to 
# vo default value ko le le.

# def attendance(name,status="absent"):
# 	print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")

#################################################################################

## code debug

## quen-1
# def greet(*names):
# 	for name in names:
# 		print("Welcome", name)

# greet("Rinki", "Vishal", "Kartik", "Bijender")
# ans * is missing in parametre because for unlimited argument we need *

##quen-2  bug- second argument was not in first call i added 12 there

# def info(name, age):
# 	print(name + " is " + age + " years old")

# info("Sonu",'12')
# info("Sana", "17")
# info("Umesh", "18") 

## quen-3  third argument was not in call section so i added there amol

# def studentDetails(name,currentMilestone,mentorName):
# 	print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","amol")

####################################################################################

## functions-question2

# def function_print_lines(name,founder):
# 	print("mera name "+ name + " hai")
# 	print("mai "+ founder + " ka co-founder hu")

# function_print_lines("pradeep","pk institute")

############################################################################

# ## Question2
# def student_name(*a):
# 	print(a)

# student_name("pk","ck","dk","nk","sk")

## Question 2 (Part 2)

# def isGreaterThen20(20,b):    *****doubt have to ask this questions
# 	if b>20:
# 		print("true")
# 	else:
# 		print("false")

# isGreaterThen20(15)

############################################################################
## functions-question3

# #Write add_numbers function here

# def add_numbers(num1,num2):
# 	z=num1+num2
# 	print("sum=",z)

# add_numbers(2,6)

## functions-question3(part-2)

#def add_numbers_list(list(num1),list(num2)):   # have to find the solution




#################################################################################

## functions-question4

# def check_numbers(a,b):
# 	if (a and b)%2==0:
# 		print("dono divisible hai")
# 	else:
# 		print("dono divisible nahi hai")

# check_numbers(2,4)
# check_numbers(8,7)

## functions-question4(part-2)

# def  check_numbers_list(a,b):       ### have to find solution of this questions
# 	for 



#####################################################################################

## functions-return_values

## How to return a value from a function?

## functions-question5

# def calculator(number_x, number_y, operation):   ## find solution for this not known
# 	add=number_x+number_y
# 	return add
# 	sub=number_x-number_y
# 	return sub
# 	mult=number_x*number_y
# 	return mult
# 	divide=number_x/number_y
# 	return divide

# result=calculator(4,5,"mult")
# print(result)

## Question (Part 2)







## Question (Part 3)

################################################################################

## innerFunction        not working have to find error and resolved

# def first_function():
# 	s = 'I love India'
# 	def second_function():
# 		s = "MY NAME IS JACK"
# 		print(s)  
# 	second_function()
# 	print(s) 
 
# first_function()

##OUTPUT:-

# MY NAME IS JACK

# I love India


#####################################################################################
## InTRO

## QUESTion-1

# def eligibleforvote(age):
# 	if age>=18:
# 		print("you are eligible for vote")
# 	else:
# 		print("you will be eligible after ",18-age,"year")

# eligibleforvote(17)
# eligibleforvote(19)	

##################################################################################
##  Question 2

# def perfect(n):
# 	s=0
# 	#n=int(input("Enter number :"))
# 	for k in range(1,n):
# 		if n%k==0:
# 			s=s+k
# 	if s==n:
# 		print(n,"is perfect number")
# 	else:
# 		print(n,"not perfect number")
# perfect(6)
# perfect(28)

#####  2nd qestion of question-2    ## have to ask all perfect no from 1 to 1000

# def perfect():
# 	for inp in range(1,1001):
# 		ls=[]
# 		for i in range(1,inp):
# 			if inp%i==0:
# 				ls.append(i)
# 	sum=0
# 	for i in ls:
# 		sum=sum+i
# 	if sum==inp:
# 		print(inp)
# perfect()

# def perfect(n):
# 	for i in range(1,n):
# 		s=0
# 		for k in range(1,n):
# 			if n%k==0:
# 				s=s+k
# 		if s==n:
# 			print(n,"is perfect number")
# 		else:
# 			print(n,"not perfect number")

##########################################################################

## Question 3

# def sumaverage():
# 	s=0
# 	for i in a:
# 		s=s+i

# 	sum=s
# 	avg=sum/3
# 	print("sum of three no=",sum ,"\naverage of no= ",avg)
# for i in range(3):
# 	a=[]
# 	v=int(input("enter the number:"))
# 	a.append(v)
# sumaverage()

#########################################################################

## Question 4

# def shownumbers(limit):
# 	for i in range(0,(limit+1)):
# 		if i%2==0:
# 			print(i,"even")
# 		else:
# 			print(i,"odd")
# shownumbers(8)

##########################################################################

## Question 5            some bugs here all multiple number not showing in place of mulftiple are 

# def multiple3and5(limit):
# 	sum=0
# 	for i in range(0,(limit+1)):
# 		a=[]
# 		if i%3==0 or i%5==0:
# 			sum=sum+i
# 			a.append(i)
# 	print("multiple are=",a,"\nsum=",sum)

# multiple3and5(10)

###########################################################################

# questions -6

# def checkKey():
# 	car ={
# 	"brand":  "ford",
# 	"model":  "mustang",
# 	"year":  1964
# 	}
# 	if "model" in car:
# 		print("Yes, 'model' is one of the keys in the thisdict dictionary.")
# 	else:
# 		print("No, 'model' key dictionary mai nahi hai.")

# checkKey()

##########################################################################3

## question6

# def speed_checker(speed):
# 	if speed>70:
# 		if speed>70 and speed<=75:
# 			print("point1")
# 		if speed>75 and speed<=80:
# 			print("point2")
# 		if speed>80 and speed<=85:
# 			print("point3")
# 		if speed>85 and speed<=90:
# 			print("point4")
# 		if speed>75 and speed<=80:
# 			print("point5")
# 		if speed>75 and speed<=80:
# 			print("point6")
# 		if speed>75 and speed<=80:
# 			print("point7")
# 		if speed>75 and speed<=80:
# 			print("point8")
# 		if speed>75 and speed<=80:
# 			print("point9")
# 		if speed>75 and speed<=80:
# 			print("point10")
# 		if speed>75 and speed<=80:
# 			print("point11")
# 		if speed>75 and speed<=80:
# 			print("point12, your licenced is suspended")
# 	else:
# 		print("okey")

# speed_checker(60)
# speed_checker(90)

########################################################################

## question7

# def stringlengthcheck(a,b):
# 	if len(a)>len(b):
# 		print(a)
# 	elif len(a)<len(b):
# 		print(b)
# 	else:
# 		print(a)
# 		print(b)
# c=input("enter your word: ")
# d=input("enter your word: ")
# stringlengthcheck(c,d)

###############################################################################

## question8

# def numberindictionary(number):
# 	# dict={}
# 	# for i in range (1,number+1):
# 	c=dict()
# 	for i in range(1,number+1):
# 		c.update({i:i*i})
# 	print(c)
# numberindictionary(5)
# numberindictionary(20)

###############################################################################
## INTRO PART-II

## question1
# def employee(name,salary=20000):
# 	print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")

###################################################################################

## question-2   have to find error indentation

# def primeorNot(num):
# 	if num > 1:
# 		for i in range(2,num):
# 			if (num % i) == 0:
# 				print(num,"is not a prime number")
# 	print(i,"times",num//i,"is",num)
# 		break
#    			else:
# 				print(num,"is a prime number")

# 	else:
# 		print(num,"is not a prime number")
# primeorNot(406)

####################################################################################
 ## Questions-3

# def greet(*names):
# 	for name in names:
# 		print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

#######################################################################

## Question 4

# def sumofdigits(number):
# 	sum = 0
# 	modulus = 0
# 	while number!=0 :
# 		modulus = number%10
# 		sum+=modulus
# 		number/=10
# 	return sum

# print(sumofdigits(123))

#######################################################################

## question5


# def  meal(day,time):
# 	if day=="sunday":
# 		if time=="breakfast":
# 			return "dosa"
# 		elif time=="lunch":
# 			return "dal rice"
# 		elif time=="dinner":
# 			return "paneer and  chapati"
# 		else :
# 			return "time not found"
# 	elif day=="monday":
# 		if time=="breakfast":
# 			return "fried rice"
# 		elif time=="lunch":
# 			return "aloo rice"
# 		elif time=="dinner":
# 			return "chhole bhature"
# 		else :
# 			return "time not found"
# 	elif day=="other":
# 		if time=="breakfast":
# 			return "aloo"
# 		elif time=="lunch":
# 			return "rajma rice"
# 		elif time=="dinner":
# 			return "veg-chapati"
# 		else :
# 			return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))

##########################################################

## question6

# def checkKey():
# 	car ={
# 	"brand":  "ford",
# 	"model":  "mustang",
# 	"year":  1964
# 	}
# 	if "model" in car:
# 		print("Yes, 'model' is one of the keys in the thisdict dictionary.")
# 	else:
# 		print("No, 'model' key dictionary mai nahi hai.")

# checkKey()

######################################################################

## intro 3

## questions-1  i did its debuge only adding calculate in calling function

# def calculate_sum(a,b):
# 	sum = a+b
# 	print(sum)
# calculate_sum(4,5)

#######################################################################

## Question 2  debuge-i add def in starting by removing function from there 

# def multi(a,b):
# 	multiply=a*b
# 	return multiply
# print(multi(3,4))

##############################################################################

## Question 3 debuge-d was capital in place of Def ,in print replace sum by avg/3

# def Avg(number1,number2,number3):
# 	avg=number1+number2+number3
# 	print(avg/3)
# Avg(1,3,2)

#######################################################################

## Question 4  debuge-indentation space was not there so gave that

# def voter(age):
# 	if age >=18:
# 		print("eligible")
# 	else:
# 		print("not eligible")
# voter(20)

####################################################################################

## Question 5

# def distance(kms):
# 	if kms < 20:
# 		print("close")
# 	elif kms < 50:
# 		print("median")
# 	else:
# 		Print("far")
# distance(20)

