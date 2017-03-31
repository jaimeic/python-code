# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:14:41 2016

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, neighbors, metrics, cross_validation

#Import Data into Python
ep_data = np.genfromtxt('ep_data.csv',delimiter=",")
ep_labels = np.genfromtxt('ep_labels.csv',delimiter=",")


#Create KNN Classifier, Leave One Out indeces and predictions matrix
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
loo = cross_validation.LeaveOneOut(20)
predictions = np.zeros((20,1))

#Train and test 20 instances of classifier
for index_train, index_test in loo:
    knn.fit(ep_data[index_train,:], ep_labels[index_train])
    predictions[index_test] = knn.predict(ep_data[index_test])

#Check to see correct predictions
is_correct = np.zeros((20,1))
for i in range(len(predictions)):
    is_correct[i] = predictions[i] == ep_labels[i]
    
accuracy = sum(is_correct)/len(is_correct)*100





plt.scatter(ep_data[:11,11],ep_data[:11,16],color='red')
plt.scatter(ep_data[11:,11],ep_data[11:,16],color='blue')
plt.xlabel('Saccade Frequency (counts/sec)')
plt.ylabel('Saccade Latency (ms)')
plt.title('Expert vs Novice EP')
plt.show()






ep_saccadefreq = ep_data[:,11]
ep_saccadelat = ep_data[:,16]


df = pd.DataFrame(dict(ep_saccadefreq=ep_saccadefreq, ep_saccadelat=ep_saccadelat, ep_labels=ep_labels))

#fig, ax = plt.subplots()
#
#colors = {'1':'red', '0':'blue'}
#
#ax.scatter(df['ep_saccadefreq'], df['ep_saccadelat'], c=df['ep_labels'].apply(lambda x: colors[x]))
#plt.show()

groups = df.groupby('ep_labels')

fig, ax = plt.subplots()
ax.margins(0.05)
for name, group in groups:
    ax.plot(group.ep_saccadefreq, group.ep_saccadelat, marker='o', linestyle = '',  label=name)
ax.legend()

plt.show()
    
    
    





