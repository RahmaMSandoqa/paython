emp1 = Employee('Ahmad Yazan',
				'Amman,Jordan',
				1000,
				500,
				'HR Consultant', 
				[434, 200, 1020])
emp2 = Employee('Hala Rana', 
				'Aqaba,Jordan', 
				2000, 
				750, 
				'Department Manager', 
				[150, 3000, 250])
emp3 = Employee('Mariam Ali', 
				'Mafraq,Jordan', 
				3000, 
				600, 
				'HR S Consultant', 
				[304, 1000, 250, 300, 500, 235])
emp4 = Employee('Yasmeen Mohammad', 
				'Karak,Jordan', 
				4000, 
				865, 
				'Director', 
				[])
#1
employees = [
		Employee('Ahmad Yazan', 'Amman,Jordan', 1000, 500, 'HR Consultant', [434, 200, 1020]),
		Employee('Hala Rana', 'Aqaba,Jordan', 2000, 750, 'Department Manager', [150, 3000, 250]),
		Employee('Mariam Ali', 'Mafraq,Jordan', 3000, 600, 'HR S Consultant', [304, 1000, 250, 300, 500, 235]),
		Employee('Yasmeen Mohammad', 'Karak,Jordan', 4000, 865, 'Director', [])
		]

stu1 = Student('Khalid Ali', 'Irbid, Jordan', 20191000,'History', 
			   {
	   'English': 80,
	   'Arabic': 90,
	   'Art': 95,
	   'Management': 75
	   })
stu2 = Student('Reem Hani', 'Zarqa, Jordan', 20182000,'Software Engineering', 
			   {
	   'English': 80, 
	   'Arabic': 90, 
	   'Management': 75, 
	   'calculus': 85, 
	   'OS': 73, 
	   'programming': 90
	   })
stu3 = Student('Nawras Abdullah', 'Amman, Jordan', 20161001, 'Arts', 
			   {
	   'English': 83, 
	   'Arabic': 92, 
	   'Art': 90, 
	   'Management': 70
	   })
stu4 = Student('Amal Raed', 'Tafelah, Jordan', 20172030, 'Computer Engineering', 
			   {
	   'English': 83,
	   'Arabic': 92, 
	   'Management': 70, 
	   'calculus': 80, 
	   'OS': 79, 
	   'programming': 91
	   })
#1, 2	
employees = [emp1, emp2, emp3, emp4]
students = [stu1, stu2, stu3, stu4]
#2
students = [
		Student('Khalid Ali', 'Irbid, Jordan', 20191000,'History', 
		  {
	 'English': 80,
	 'Arabic': 90,
	 'Art': 95,
	 'Management': 75
	 }),
	Student('Reem Hani', 'Zarqa, Jordan', 20182000,'Software Engineering', 
		 {
	'English': 80, 
	'Arabic': 90, 
	'Management': 75, 
	'calculus': 85, 
	'OS': 73, 
	'programming': 90
	}),
	Student('Nawras Abdullah', 'Amman, Jordan', 20161001, 'Arts', 
		 {
	'English': 83, 
	'Arabic': 92, 
	'Art': 90, 
	'Management': 70
	}),
	Student('Amal Raed', 'Tafelah, Jordan', 20172030, 'Computer Engineering', 
		 {
	'English': 83,
	'Arabic': 92, 
	'Management': 70, 
	'calculus': 80, 
	'OS': 79, 
	'programming': 91
	})
	]

#3, 4
numOfEmployees = len(employees)
@@ -319,7 +302,7 @@ def AStudents(students):
print('SALARIES:')
print('The Highest Salary =', highestSalary, '\bJOD')
print('The Lowest Salary =', lowestSalary, '\bJOD')
print('Total Salaries =', totalSalaries, '\bJOD')
print('Total Salaries =', totalSalaries, '\bJOD', end='\n\n')

#17
del employees, students 