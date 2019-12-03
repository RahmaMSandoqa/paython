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
##Day8
#import pandas as pd
#data = [100, 120, 140, 180, 200, 210, 214]
#s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
#
#print(s)
#
##print (s.describe())
#s.plot(kind="bar")
#print (s.agg(["sum","max"]))
#s.plot()
#=============================================
#import numpy as np
#import pandas as pd
#dates = pd.date_range('20190101', periods=8)
#df= pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS'))
##print(df.head())
#print(df['P'])
#===========================================
#import numpy as np
#import pandas as pd
#dates = pd.date_range('20190101', periods=8)
#df= pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS'))
##print(df.head())
#print(df[0:1])
##print(df['20190102':'20190104'])
#==========================================

#import numpy as np
#import pandas as pd
#dates = pd.date_range('20190101', periods=8)
#df= pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS'))
##print(df.head())
#print(df.iloc[:, 1:3])
#============================================
#import pandas as pd
#import numpy as np
#d = {'one':[1,2,3,4,5],
#     'two':[2,2,2,2,2],
#     'letter':['a','a','b','b','c']}
#
#df= pd.DataFrame(d)
#df.to_csv('myDataFrame.csv', sep='\t')
#print(df)
#print( df['one'].apply( np.sqrt) ) 
#print( df['letter'].map(lambda x : 'map_' + x) )

#=============================================
#import pandas as pd
#df= pd.read_csv('myDataFrame.csv',sep='\t',index_col=0)
#print(df) 
#============================================
#import pandas as pdd = {'one':[10,20,5,40,70,10,20,5,40,70],
#                          'two':[14,0,30,40,20,14,0,70,40,20]}
#df= pd.DataFrame(d,columns=["one", "two"])
#df.plot()
#======================================
#DAY9
#import statistics as st
#import random
#x =[3,1.5,4.5,6.75,2.25,5.75,2.25]
#print(st.mean(x))
#print(st.harmonic_mean(x))
#print(random.random())
#=========================================
#import math
#n = 100.2
#print(math.floor(n))
#print(math.ceil(n))
#
#=====================================
#import doctest
#def sum(a,b):
#    """
#    calculates the sum
#    >>> sum(1,1)
#    3
#    >>> sum(1,-1)
#    0
#    >>> sum(-1,-1)
#    -2
#    >>> sum(0,-10)
#    -10
#    >>>
#    """
#    return a*b
#if __name__=="__main__":
#    doctest.testmod(verbose = True)

#====================================
#from PIL import Image
#size =(128,128)
#saved = "cat.jpg"
#try:
#    im=Image.open("cat.jpg")
#except:
#    print("unable")    
#original = Image.open("cat.jpg")
#blurred = original.filter(ImageFilter.BLUR)
#im.thumbnail(size)
#im.save(saved)
#original.show()
#blurred.show()
#blurred.save("cat.jpg")
#====================================
#from PIL import Image
#image = Image.open("cat.jpg")
#greyscale_image = image.convert("L")
#greyscale_image.show()
#=====================================

#import sympy as sym
#x = sym.symbols('x')
#expr = x + 1
#print ( expr.subs(x, 2) )

#=====================================
#import sympy as sym
#x = sym.symbols('x')
#expr= x + x**2 + 1
#print( expr.subs(x, 2) )
#====================================
#from sympy import *
#x = symbols('x')
#init_printing()
#expr = Integral(sqrt(1/x),x)
#print(expr)
#===================================
#import sympy as sym
#x = sym.Symbol('x')
#y, i ,n, a, b = sym.symbols('y i n a b')
#print(  sym.expand( (x + y) ** 3 )   )
#print ( sym.limit(sym.sin(x)/ x, x,0))
#print (sym.integrate(6 * x ** 5,x))
#print ()
#=====================================
#solution = sym.solve((x + 5 * y -2, -3 * x + 6 
#* y -15), (x, y))
#print(solution[x], solution[y])
#====================================
#from sympy import symbols
#from sympy.plotting import plot3d
#x, y = symbols('x y')
#f=cos(x)+sin(y) 
#plot3d(f, (x, -10, 10), (y, -10, 10))
#===================================
#import xlsxwriter
#workbook = xlsxwriter.Workbook("rahmaex.xLsx")
#worksheet = workbook.add_worksheet()
#worksheet.autofilter("A1:B4")
#
#data = ["mark",10,20,30,50,40,60]
#
#format = workbook.add_format()
#format.set_bold()
#format.set_font_color("red")
#format.set_font_size(10)
#
#worksheet.write_column("A1",data,format)
#worksheet.write_comment("B2","this is a comment")
#
#
#format2= workbook.add_format({"bold":True,"font_color": "blue"})
#worksheet.write_column("B1",data,format2)
#workbook.close()
#
#===============================================================
#from xlrd import open_workbook
#
#wb = open_workbook("rahmaex.xLsx")
#
#for s in wb.sheets():
#    print("sheet:",s.name)
#    for row in range(s.nrows):
#        values = []
#        for col in range(s.ncols):
#            values.append(s.cell(row,col).value)
#        print(",".join(str(values)))
#================================================================
#from tkinter import *
#import tkinter as tk
#
#root = Tk(className=" My First GUI ")
#fw = 300
#fh = 150
#x  = ( root.winfo_screenwidth() - fw ) / 2
#y  = ( root.winfo_screenheight() - fh ) / 2 - 50
##root.geometry("300x150+50+50")
#root.geometry( '%dx%d+%d+%d' %(fw,fh,x,y) )
#root.mainloop()
#top.geometry("200*100")
#b = button(top,text = "try")
#b.pack()
#top.mainloop()
#root = tk.Tk()
#label = tk.Label(root,text="Hello world", padx=10, pady=10)
#label.pack()
#root.mainloop()
#=========================================        
#from tkinter import *
#top = Tk()
#top.geometry("200x100")
#b = Button( top,text = "simple")
#b.pack()
#top.mainloop()
        
#==========================================
#from tkinter import *
#from tkinter import messagebox
#def pressed():
##    print ("hello iam rahma")
#    answer = messagebox.askquestion("jjjjj","oihiugig")
#    if answer == "yes":
#        print("i like")
#    else:
#        print("no")
#root = Tk()
#button = Button(root,text = "rahma", command = pressed)       
#button.pack(pady = 40, padx = 40)
#root.mainloop()
#        
#=============================================        
#from tkinter import *
#
#win = Tk()
#v = StringVar()
#e = Entry(win,textvariable = v)
#e.pack()
#v.set("rahma sandoqa")
#print(v.get())
#win.mainloop()        
#================================================
#from tkinter import *
#root = Tk(className="my first")
#svalue = StringVar()
#w = Entry(root,textvariable=svalue)
#w.pack()
#def act():
#    print("your entered")
#    print("%s" % svalue.get())
#foo = Button(root,text="press me",command=act)
#foo.pack()
#root.mainloop()       
#================================================
#from tkinter import *
#root = Tk()
#root.title("menu_win")
#def notdone():
#    messagebox.showinfo("not implemented","not yet available")
#top = Menu(root)
#root.config(menu=top)
#
#
#file = Menu(top,tearoff=0)
#file.add_command(label="new",command=notdone)      
#file.add_command(label="open",command=notdone)        
#file.add_separator()
#file.add_command(label="quit",command=root.destroy)
#top.add_cascade(label="file",menu=file)
#
#
#edit = Menu(top,tearoff=0)
#edit.add_command(label="cut",command=notdone)
#edit.add_command(label="past",command=notdone)
#top.add_cascade(label="edit",menu=edit)
#root.mainloop()
#=================================================
#from tkinter import *
#from tkinter.colorchooser import *
#def getColor():
#    color = askcolor()
#    print(color)
#Button(text="select",command=getColor).pack()
#mainloop()    

#=====================================================
       
        
        
        
        
        
        
        