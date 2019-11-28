#1
#import pandas as pd
#d = pd.Series([2, 4, 6, 8, 10])
#print(d)
#============================================
#2
#import pandas as pd
#d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800} 
#series = pd.Series(d1)  
#print(series)
#============================================
#3
#import pandas as pd
#data =  [20, 10, 150, 110, 100, 50]
#s = pd.Series(data)
#print( s.describe())
#s.plot(kind="bar", color=("red","black","green","blue","yellow","#33fbf4"))
#==========================================
#4
#import pandas as pd
#data2 = {'d1':[100,200,5,400,700,100,200,50,400,700],
#         'd2':[140,0,300,400,200,140,0,700,400,200]}
#
#d3 = pd.DataFrame(data2)
#d3.plot()
#=========================================
#5
#dataArr = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
#
#d4 = pd.DataFrame(dataArr)
#print(d4)
#========================================
#6
#dataCircle={
#        'names' : ['Bob','Jessica','Mary','John','Mel'],
#        'births' : [968, 155, 77, 578, 973]}
#
#df = pd.DataFrame(dataCircle)
#df.plot.pie(y='births', figsize=(5, 5))
#===========================================
#7
#dataPands = [100, 2200, 300, 400, 600, 700, 800, 900]
#
#dataFrame = pd.DataFrame(dataPands, columns = ["Number"])
#print(dataFrame)
#
#dataFrame.to_csv('data_csv.csv', sep='\t')
#dataFrame.to_csv('data_comma.csv', sep=',')
#pd.read_csv('data_csv.csv',sep='\t',index_col=0)
#=======================================