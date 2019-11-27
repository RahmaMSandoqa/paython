# Seventh Day Exercise
import numpy as np
import matplotlib.pyplot as plt

print('EXERCISE 1') 
ex1 = np.array([np.zeros((1,10), dtype=int), 
				  np.ones((1, 10), dtype=int), 
				  np.ones((1, 10), dtype=int)*5])
print(ex1)
#==============================================================================
print('\n\nEXERCISE 2')
vector = np.arange(30, 71)
print(vector)
#==============================================================================
print('\n\nEXERCISE 3') 
evenVector = np.arange(30, 71, 2)
print(evenVector)
#==============================================================================
print('\n\nEXERCISE 4') 
identityMatrix = np.identity(3, dtype=int)
print(identityMatrix)
#==============================================================================
print('\n\nEXERCISE 5') 
random = round(np.random.random(), 2)
print(random)
#==============================================================================
print('\n\nEXERCISE 6') 
matrix = np.array([[1, 2, 3, 4],
			 [2, 4, 6, 8],
			 [4, 8, 12, 16]])

for row in matrix:
	print('For row', row, 'values = ', end='')
	for col in row:
		print(col, ',', end='\b ')
		
	print()
#==============================================================================
print('\n\nEXERCISE 7') 
negVector = np.arange(0, 21)
print('Before: ',negVector)

for index in range(0, len(negVector)):
	num = negVector[index] 
	if num >= 9 and num <= 15:
		negVector[index] = -num 
		
print('After: ',negVector)
#==============================================================================
print('\n\nEXERCISE 8') 
x = np.array([1,8,3,5])
y = np.random.randint(0,11,4)
multiplication = x*y

print('X= ', x)
print('Y= ', y)
print('X*Y = ', multiplication)
#==============================================================================
print('\n\nEXERCISE 9') 
def findRowsCols(matrix): 
	print('Matrix:\n',matrix)
	return matrix.shape 

matrix = np.ones((3,4), dtype=int)
rows, cols = findRowsCols(matrix) 

print('Number of Rows = ', rows)
print('Number of Columns = ', cols)
#==============================================================================
print('\n\nEXERCISE 10') 
threeBythree = np.arange(27).reshape(3,3,3)
print(threeBythree)
#==============================================================================
print('\n\nEXERCISE 11') 
a = np.array([9,-1,2,5])
b = np.array([1,-6,0,10])
c = np.array([[1,8,2,5],[3,1,7,9]])

print("a = ", a) 						# [ 9 -1  2  5]
print("b = ", b)						# [ 1 -6  0 10]
print("c = ", c)						# [[1 8 2 5]
									    #  [3 1 7 9]]
print("a-b: ", a-b)						# [ 8  5  2 -5]
print("a*b: ", a*b)						# [ 9  6  0 50]
print("a.dot(b): ", a.dot(b)) 	 	 	# 65
print("a*2: ", a*2)						# [18 -2  4 10]
print("np.sin(a): ", np.sin(a)) 	 	# [ 0.41211849 -0.84147098  0.90929743 -0.95892427]
print("a<3: ", a<3)						# [False  True  True False]
print("a.sum(): ", a.sum()) 	 	 	# 15
print("a.sum(axis=0): ", a.sum(axis=0)) # 15
print("c.sum(): ", c.sum()) 	 	 	# 36
print("c.sum(axis=0): ", c.sum(axis=0)) # [ 4  9  9 14]
print("a.min(): ", a.min()) 			# -1
print("a.max(): ", a.max())				# 9
print("a.mean(): ", a.mean()) 	 	 	# 3.75
print("a average(): ", np.average(a)) 	# 3.75
print("a median(): ", np.median(a))  	# 3.5
print("a std(): ", np.std(a))  	 	 	# 3.6996621467371855
print("a var(): ", np.var(a)) 	 	 	# 13.6875
print("c.cumsum(): ", c.cumsum()) 	 	# [ 1  9 11 16 19 20 27 36]
print("a[1:2] : ", a[1:2])				# [-1]
print("a[2:] : ", a[2:])				# [2 5]
print("c[-1] : ", c[-1])				# [3 1 7 9]
#==============================================================================
print('\n\nEXERCISE 12') 
ax = plt.axes()
ax.set_facecolor("white")

x = range(1, 50)
y = [value * 3 for value in x]

plt.plot(x, y, color="blue")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')

plt.show()
#==============================================================================
print('\n\nEXERCISE 13') 
ax = plt.axes()
ax.set_facecolor("white")

x1 = [10,20,30]
y1 = [20,40,10]

x2 = [10,20,30]
y2 = [40,10,30]

plt.plot(x1,y1,label="Line 1")
plt.plot(x2,y2,label="Line 2")

plt.legend()
plt.title('Two or more lines on same plot with suitable legends')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.show()
#==============================================================================
print('\n\nEXERCISE 14') 
ax = plt.axes()
ax.set_facecolor("white")

t = np.arange(0., 5., 0.2)
t2=t**2
t3=t**3

plt.plot(t, t, 'g--', t, t2, 'bs', t, t3, 'r^')
plt.title('Figure 14')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.show()
#==============================================================================
print('\n\nEXERCISE 15')  
ax = plt.axes()
ax.set_facecolor("white")

programmingLanguages= ['Python','Java', 'PHP', 'JavaScript', 'C#', 'C++']
popularity=[22.2, 17.6, 8.8, 8, 7.7, 6.7]

x= [i for i, _ in enumerate(programmingLanguages)]
plt.bar(x, popularity,color=("red","black","green","blue","yellow","lightblue"))
plt.xticks(x, programmingLanguages)
plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Popularity Of Programming Language")

plt.show()