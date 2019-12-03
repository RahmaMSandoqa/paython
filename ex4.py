#ex1
#o=lambda x=1,y=2,z=3:x+y+z
#print(o())
#print(o(10))
#print(o(10,20))
#output:(6,15,33)
#================================================
#ex2
#number = [5, 7, 4,6,3,8]
#final_list = list(map(lambda x: x*2 , number))
#print(final_list)
#===============================================
#ex3
#print((lambda x,y:x*y)(4,5))
#================================================
#ex4
#print(list(filter(lambda x: x<0, range(-5,5))))
#
#================================================\
#ex5
#x= lambda a,b,c:a+b+c
#print(x(5,6,2))
#output:13
#==================================================
#ex6
#x= ("Joey","Monica","Ross")
#y= ("Chandler","Pheobe")
#z= ("David","Rachel","Courtney")
#print(list(zip(x,y,z)))
#output:[('Joey', 'Chandler', 'David'), ('Monica', 'Pheobe', 'Rachel')]
#================================================
#ex7
#coin= ("Bitcoin","Ether","Ripple","Litecoin")
#code=("BTC","ETH","XRP","LTC")
#d=dict(zip(coin,code))
#print(d)
#--------------------------------------------------
#ex8
#def fun(v):
#    letters = ["a","e","i","o","u"]
#    if v in letters:
#        return True
#    else:
#        return False
#    
#sequence = ["g","j","e","j","o","p","r"]
#filtered = list(filter(fun , sequence))
#print(filtered)
#output=['e', 'o']
#==================================================
#9
#x=list(map(int, input("Enter").split()))
#print("list of students:",x)
#
#
#-----------------------------------
#10
#def newfunc (a):
#    return a*a
#x = list(map(newfunc,(1,2,3,4)))
#print(x)
#
#========================================
#11
#def func(a,b):
#    return a+b
#a= list(map(func, [2,4,5],[1,2,3,2,4]))
#print(a)
#([3, 6, 8])
#======================================
#12
#c=map(lambda x:x+x, filter(lambda x:(x>=3),(1,2,3,4)))
#print(list(c))
#=====================================
#13
#
#c=filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))
#print(list(c))
#
#===================================
#14
#from functools import reduce
#nums = [1,2,3,-9,4]
#
#result =reduce(lambda first, nex: first if first < nex else nex, nums)
#
#print(result)
#========================================
#15
#number=[1,2,3]
#letters=['a','b','c']
#result = list(zip(number,letters))
#print(result)
#
