#Rahma = "hello rahma"
#print ("Rahman\bmaher")
#
#------------------------------------------------------------------
#age = int(input("what is your Age?"))
#print (age)
#print (type(age))
#x, y, z = "rahma","lojen","rashed"
#print(x)
#print(y)
#print(z)
#-----------------------------------------------------------------
#DAY 2
#
#a,b = 1,10
#if a >b:
#    print("a > b")
#elif a <b:
#    print("a < b")
#else:
#    print("a = b").                                                               
#
#
#
#a,b,c=1,10,55
#max = a if (a > b > c) else c 
#print(max)
#
#-----------------------------------------------------------
#if 'rahma' in ['ahmad','rahma','hamzeh']:
#    print('rahma in a list')
#else: print('rahma not ')
#
#a =100
#b =330
#print ('a') if a > b else print ("=") if a == b else print("b")
#
#
#a= int(input("inter number"))
#b= int(input("inter number"))
#if ( a > b ):
#    print( b ,a)
#else:
#    print( a, b)
#
#
#-----------------------------------------------------------------
#name = (input("enter your name"))
#age = int(input("enter your age"))
#
#if ( age < 18 ):
#    print("under age ")
#    Average= int(input("enter your Average"))
#    if(Average >= 90):
#        print("Excellent Average")
#    elif(Average >= 50 >90):
#        print("passed")
#    else:
#        print("failed")
#    
#    
#else:
#    job =(input("what your job?"))
#    print("age,job")
#------------------------------------------------------------------
#
#for rahma in range(9):
#    print(rahma)
#---------------------------------
#for a in range(0,6,9,6,2):
#    print(a)
#---------------------------------
#for x in "name":
#    print(x)
#====================================
#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
#    print(x)
#    if x == "banana":
#        break
##------------------------------------
#
#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
#    if x == "banana":
#        continue
#    print(x)
#
#---------------------------------------------
#
#for x in range(6):
#    print(x)
#else:
#    print("Finally finished!")
#--------------------------------------------------
#while True:
#    a=input('>')
#    if a=='exit':
#        break
#    print (a)
#---------------------------------------------------
#i =0
#while i<10:
#    print("*")
#    i+=1
#
#----------------------------------------------------
#i =0
#while i<31:
#    print("*" , end='')
#    i+=1
#---------------------------------------------------
#
#
#for x in range(10):
#    for i in range(x):
#       print("*",end="")
#    print()
#
#-------------------------------------------------
#for x in range(8):
#    for i in range(x):
#       print("",end="")
#       X+=1
#    for i in range(x):
#       print("*",)
#    print()
#
#while True:
#     try:
#         n = input("Please enter an integer: ")
#         n = int(n).
#         break
#
#================================================
#DAY4
#def my_function(food):
#   for x in food:
#     print(x)
#fruits = ["apple", "banana", "cherry"]
#my_function(fruits)

#------------------------------------------------------
#def myfun(**kwargs):
#    for key, value in kwargs.items():
#        print("%s == %s" %(key,value))
#myfun(first='Geeks',mid='for',last='geeks')
#---------------------------------------------------
#def factorial(n):
#    if n ==1:
#        return 1
#    else:
#        return n * factorial(n-1)
#print(factorial(5))
#====================================================
#sum = lambda x,y,z :x * y *z
#print (sum(1,2,3))
#
#=====================================================
#areas = [1,5,6,6,8,7]
#rahma = list(map(lambda x:x*2,areas))
#print(rahma)
#-------------------------------------------------
#mark = [66,90,68,76,80,74]
#number= list(filter(lambda x:x >, mark))
#print(number)
#=================================================
#DAY5
#class person:
#    
#    
#    def __init__(self,name) :
#        self.name = name
#    def whoami(self):
#        return"Iam"+self.name
#    def __del__(self):
#        print('i deleted')
#                
#p1 = person('tom')
#print(p1.whoami())
#print(p1.name)
#del p1
#
#==================================================
#class Encapsulation():
#    def __init__(self,a,b,c):
#        self.Apublic = a
#        self._Bprotected = b
#        self.__Cprivate =c
#    def getprivate(self):
#         return self.__Cprivate
#    def setprivate(self,n):
#        self.__Cprivate=n
#x = Encapsulation(11,13,17)
#print ( x.Apublic )
#print ( x._Bprotected )
##print ( x.__Cprivate)
#print ( x.getprivate())
#x.setprivate(2)
#print ( x.getprivate())
#        
#
#============================================
#class A():
#    def __init__(self):
#        print("rahma")
#class B(A):
#    def __init__(self):
#        print("hello") 
#        super().__init__()
#        A.__init__(self)
#b1=B()        
#
#===============================================
#class circle:
#    def __init__(self,redius):
#        self.__redius = redius
#        
#    def setRadius(self,redius):
#        self.__rediusc = redius 
#
#    def getRedius(self):
#        return self.__redius
#    def __add__(self,another_circle) :
#
#        return circle(self.__redius + another_circle.__redius )
# c1 = Circle(4)
# print(c1.getRadius())
# c2 = Circle(5)
# print(c2.getRadius())
# c3 = c1 + c2
# print(c3.getRadius())   
#======================================================
#DAY7
#b = np.array([1,4,7,5])
#print(b)
#


#c = np.array([[1,4,7,5],[2,8,3,2]])
#print(c)
#

#a = np.array([[1,2,3,5,4,67,9,6,4],[9,4,5,4,6,5,7,9,6]])
#print('\n quicksort:')
#print(a)
#print(
#      )

#import matplotlib.pyplot as plt
#f = [1,2,8,4,5,6]
#plt.plot(f)
#plt.show()

#plt.style.use("ggplot")
#x=[1,2,3,4,5,6]
#y=[1,4,9,16,0,30]
#
#plt.plot(x,y)
#plt.ylabel("y number")
#plt.xlabel("x number")
#plt.show()
#==============================================

#import numpy as np
#import matplotlib.pyplot as plt
#def p1(x): return x**4 -4*x**2 + 3*x 
#def p2(x): return np.sin(10*x) * 10 
#X = np.linspace(-3, 3, 200)
#plt.plot( X,p1(X), X,p2(X))
#plt.show()
#=============================================
#import numpy as np
#import matplotlib.pyplot as plt
#n = 1024
#x = np.random.normal(0,1,n)
#y = np.random.normal(0,1,n)
#
#plt.scatter(x,y)
#plt.show()

#==============================================
























