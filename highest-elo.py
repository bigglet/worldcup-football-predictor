import csv

#Read data from csv files
x_test = []
with open('data-standard/x_test.csv','rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		x_test.append(row)

y_test = []
with open('data-standard/y_test.csv','rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		y_test.append(row)

#Variables for calculating accuracy
game_count = len(x_test)
correct_count = 0.0

#for every game in the test set, predict -1 or 1
for i in range(len(x_test)):
    if( x_test[i][2] >= x_test[i][3]  ):
        if(y_test[i][0] == '1'):
            correct_count += 1
        print '1', y_test[i]
    else:
        if( y_test[i][0] == '-1' ):
            correct_count += 1
        print '-1', y_test[i]

print (correct_count/game_count)*100
