# Start out with standard ML models initially
# Then use tensorflow/keras to create a deep learning implementation of this problem

# This is a classification problem

from sklearn.linear_model import LogisticRegression
    # LogisticRegression is a linear classifier that uses
    # error minimizing formulas to come to the line of best fit
    # http://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
    # http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression

from sklearn.linear_model import SGDClassifier
    # Stochastic Gradient Descent uses convex loss functions like SVM's and Logistic Regression.
    # This function has been around for a while, but has gained popularity due to a boost of large-scale learning / big data.
    # http://scikit-learn.org/stable/modules/sgd.html

from sklearn.neighbors import KNeighborsClassifier
    # Uses the kNN algorithm as a classifier. 
    # kNN is more commonly used in unsuperivsed learning
    # http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier

from sklearn.gaussian_process import GaussianProcessClassifier
    # Uses the Gaussian processes to create probabilistic classification
    # http://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier

from sklearn.naive_bayes import GaussianNB
    # Combines Gaussian and Naive Bayes in order to create classification for probablity
    # http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB

from sklearn.tree import DecisionTreeClassifier
    # Classifier used to perform multi-class classification.
    # Decision Trees can increase in depth and complexity, which can lead to either overfitting or higher accuracy.
    # http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier

# Other modules that are needed
import numpy as np
import pandas as pd

# Read in the data into a pandas dataframe
training_set = pd.read_csv('training.csv')
testing_set = pd.read_csv('test.csv')

# Get the list of columns and set the first column to the ID
training_columns = training_set.columns.tolist()
training_columns[0] = "ID"
training_set.columns = training_columns

testing_columns = testing_set.columns.tolist()
testing_columns[0] = "ID"
testing_set.columns = testing_columns

# Save the results of the training data in a seperate var
y_train = np.array(training_set[['Made Donation in March 2007']])

# Remove the results from the training set
X_train = np.array(training_set.drop(['Made Donation in March 2007'], axis=1))
X_test = testing_set

# Fits the classifier to the training data and returns the classifier
def FitClassifier(classifier, X_train, y_train):
    return classifier.fit(X_train, y_train)

# Predicts the probability of the result given the test data and 
# returns the numpy array of it with the second column dropped
def ScoreClassifiers(classifier, X_test):
    scores  = np.array(classifier.predict_proba(X_test))
    np.delete(scores, 1, 1)
    return scores.flatten()

# Creates a pandas dataframe to export the data as a CSV file
def CreateCSV(data, filename):
    results = pd.DataFrame()
    results[''] = testing_set["ID"]
    results["Made Donation in March 2007"] = data

    # Export to CSV
    results.to_csv(filename, index=False)

# Runs all of the above functions for an easy process of testing ML algorithms
def testClassifier(classifier, filename):
    classifierFit = FitClassifier(classifier, X_train, y_train)
    classifierScores = ScoreClassifiers(classifierFit, X_test)
    CreateCSV(classifierScores, filename)


# Initialize the classifiers
testClassifier(LogisticRegression(), 'LogisticRegressionResults.csv')
StochasticGDClassifier = SGDClassifier(loss="log")
KNNClassifier = KNeighborsClassifier()
GPClassifier = GaussianProcessClassifier()
GNBClassifier = GaussianNB()
DTClassifier = DecisionTreeClassifier()
