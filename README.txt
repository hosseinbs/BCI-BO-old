BCI_BO


To start please see: BO_BCI.py, This file is the starting point to do Bayesian Optimization.



Dependencies
_______________

Python 2.7

* Numpy
* Scipy
* Scikit-learn
* Theano
* Matplotlib

This software has been tested on linux and Windows.

How to tun the program
_______________________

To run the program, run the following command in git terminal:

git clone git://github.com/hosseinbs/BCI-BO-old.git

Then run the following command: 

/bci_framework/run_bcic.py dataset_name classification_method Feature_extraction number_of_CSPs channels train_or_test

*Dataset_name = "BCICIII3b", "BCICIV2a", "BCICIV2b", "BCICIV1", "SM2"

*Classification_method = 'MLP', 'LDA', 'QDA', 'RANDOM_FOREST', 'SVM', 'LogisticRegression', 'Boosting'

*Feature_extraction = 'BP', 'logbp', 'morlet'

*Number_of_CSPs = '-1' in case of not using CSP, otherwise an integer 

*Channels = 'ALL', 'CS', 'C34', 'C34Z', 'CSP'

*Train_or_test = 'run', 'eval' -- the program should first be run with the 'run' argument, 
then to evaluate the results on the test data 'eval' should be used


Replication of the results of the framework paper
_________________________________________________

The scripts to replicate the results of the framework paper is in folder 'Batch_files'


Run on other datasets
_____________________

To run the algorithms on other datasets, copy your data to the folder 'bci_data'. Use the same format as the names already in the folder.

add a file with the name 'yourDatasetName_spec' to the folder 'bci_framework/BCI_Framework'. Files 'BCICIII3b_spec', 'BCICIV2a_spec' , ... as examples.

Format of the data

Extending the software
______________________

The software is designed to be modular. The main file of this BCI_Framework/Main.py, the function Main.run_learner_gridsearch() performs grid search on the 

hyper-parameters which are given in file 'yourDatasetName_spec'. the function Main.submit_train_learner() either submits the jobs to a cluster (which performs grid search in parallel)

(POSIX case) or runs the code on a single machine (nt case).

Class 'BCI_Framework/Configuration_BCI' reads the 'yourDatasetName_spec' file.




