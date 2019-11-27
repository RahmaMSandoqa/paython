#class Employee:
#	def __init__(self, number, name, address, salary, jobTitle):
#		self.number = int(number)
#		self.__name = str(name)
#		self.__address = str(address)
#		self.__salary = float(salary)
#		self.__jobTitle = str(jobTitle)
#
#	def getName(self):
#		return self.__name
#
#	def getAddress(self):
#		return self.__address
#
#	def setAddress(self, address):
#		self.__address = str(address)
#
#	def getSalary(self):
#		return self.__salary
#
#	def getJobTitle(self):
#		return self.__jobTitle
#
#	def printCol(self):
#		print('Employee' + str(self.number), 'Information:')
#		print('%3s Number:' % ' ', self.number)
#		print('%3s Name:' % ' ', self.__name)
#		print('%3s Address:' % ' ', self.__address)
#		print('%3s Salary:' % ' ', self.__salary)
#		print('%3s Job Title:' % ' ', self.__jobTitle, end='\n\n')
#
#	def printRow(self):
#		print('Employee' + str(self.number), 'Information: ', end='')
#		print('Number=', self.number, end=', ')
#		print('Name=', self.__name, end=', ')
#		print('Address=', self.__address, end=', ')
#		print('Salary=', self.__salary, end=', ')
#		print('Job Title "', self.__jobTitle,'\b"', end='\n\n')
#
#	def __del__(self):
#		print(self.__name, 'has been deleted')
##
#Employee1 = Employee(1, 'Mohammad Khalid', 'Amman, Jordan', 500, 'Consultant')
#Employee2 = Employee(2, 'Hala Rana', 'Aqaba, Jordan', 750, 'Manager')
#
#Employee1.printCol()
#Employee2.printRow()
#
#Employee1.setAddress('USA')
#print('Employee1 New Address:', Employee1.getAddress(), end='\n\n')
#
#del Employee1
#del Employee2 
#
#         
        
        
        