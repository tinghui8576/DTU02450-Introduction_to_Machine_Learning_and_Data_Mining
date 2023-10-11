from matplotlib.pyplot import figure, plot, xlabel, ylabel, show
import numpy as np
from scipy.io import loadmat
from sklearn.neighbors import KNeighborsClassifier
from sklearn import model_selection
from sklearn import tree
from toolbox_02450 import mcnemar
# requires data from exercise 1.5.1
from ex1_5_1 import *

# This script crates predictions from three KNN classifiers using cross-validation

# Maximum number of neighbors
L=[1, 20, 80]

CV = model_selection.LeaveOneOut()
i=0

# store predictions.
yhat = []
y_true = []
for train_index, test_index in CV.split(X, y):
    print('Crossvalidation fold: {0}/{1}'.format(i+1,N))    
    
    # extract training and test set for current CV fold
    X_train = X[train_index,:]
    y_train = y[train_index]
    X_test = X[test_index,:]
    y_test = y[test_index]

    # Fit classifier and classify the test points (consider 1 to 40 neighbors)
    dy = []
    for l in L:
        if l == 20:
            criterion='entropy'
            # dtc = tree.DecisionTreeClassifier(criterion=criterion, min_samples_split=2)
            dtc = tree.DecisionTreeClassifier(criterion=criterion, min_samples_split=1.0/N)
            dtc = dtc.fit(X_train,y_train)
            y_est = dtc.predict(X_test)
        else:
            knclassifier = KNeighborsClassifier(n_neighbors=l)
            knclassifier.fit(X_train, y_train)
            y_est = knclassifier.predict(X_test)

        dy.append( y_est )
        # errors[i,l-1] = np.sum(y_est[0]!=y_test[0])
    dy = np.stack(dy, axis=1)
    yhat.append(dy)
    y_true.append(y_test)
    i+=1

yhat = np.concatenate(yhat)
y_true = np.concatenate(y_true)
yhat[:,0] # predictions made by first classifier.
# Compute accuracy here.
M1 = np.sum(yhat[:,0]!=y_true)/len(y_true)
M2 = np.sum(yhat[:,1]!=y_true)/len(y_true)
M3 = np.sum(yhat[:,2]!=y_true)/len(y_true)
print("accuracy for M1 is ", M1, " ,for M2 is ", M2, " for M3 is", M3)
# Compute the Jeffreys interval
alpha = 0.05
[thetahat, CI, p] = mcnemar(y_true, yhat[:,0], yhat[:,1], alpha=alpha)

print("theta = theta_A-theta_B point estimate", thetahat, " CI: ", CI, "p-value", p)