import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import normalize
import numpy as np

np.set_printoptions(threshold=np.nan)
lb = LabelEncoder()

x_test = []
with open('data-custom/x_test.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        x_test.append(row)
    x_test = np.array(x_test)
    x_test[:,0] = lb.fit_transform(x_test[:,0])
    x_test[:,1] = lb.fit_transform(x_test[:,1])

x_test.astype(float)

y_test = []
with open('data-custom/y_test.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        y_test.append(row)
    y_test = np.array(y_test)


x_train = []
with open('data-custom/x_train.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        x_train.append(row)
    x_train = np.array(x_train)
    x_train[:,0] = lb.fit_transform(x_train[:,0])
    x_train[:,1] = lb.fit_transform(x_train[:,1])


y_train = []
with open('data-custom/y_train.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        y_train.append(row)
    y_train = np.array(y_train)

rf = RandomForestClassifier(random_state=0)
rf.fit(x_train, y_train.ravel())

print 'RandomForestClassifier: ', rf.score(x_test, y_test.ravel())

x_test = normalize(x_test.astype(float))
y_test = normalize(y_test.astype(float))
x_train = normalize(x_train.astype(float))
y_train = normalize(y_train.astype(float))

lr = LogisticRegression(multi_class='multinomial',solver='newton-cg')
lr.fit(x_train,y_train.ravel())

lr_score = lr.score(x_test, y_test.ravel())
print "LogisticRegression: ", lr_score

lr_predict = lr.predict(x_test)

#save logistic score
with open('model-predict.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    for i in range(lr_predict.size):
        writer.writerow( str(int( lr_predict[i] ) ) )
