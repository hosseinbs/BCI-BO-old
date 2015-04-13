import spearmint_lite
import os
import sys
os.chdir('../bci_framework')
sys.path.append('./BCI_Framework')

import Main
import Configuration_BCI

import Single_Job_runner as SJR
import numpy as np
import itertools

from time import sleep
import sklearn

import BO_BCI    

if __name__ == '__main__':
    print "Bayesian Optimization for BCI"
#     dataset = 'BCICIII3b'
#     dataset = 'BCICIV2a'
    classifier = 'LogisticRegression'
    subject_dataset_dict = {'O3':'BCICIII3b', 'X11':'BCICIII3b', 'S4':'BCICIII3b', '100': 'BCICIV2b', '200':'BCICIV2b', '300':'BCICIV2b', '400':'BCICIV2b', '500':'BCICIV2b', '600':'BCICIV2b', '700':'BCICIV2b', '800':'BCICIV2b', '900':'BCICIV2b' ,
                            '1':'BCICIV2a', '2': 'BCICIV2a', '3':'BCICIV2a', '4': 'BCICIV2a', '5':'BCICIV2a', 
                            '6':'BCICIV2a', '7':'BCICIV2a', '8':'BCICIV2a', '9':'BCICIV2a' }
    first_iteration = True
    finished = {}
            
    class Job_Params:
        job_dir = 'BCI_Framework'
        num_all_jobs = 40
        dataset = None
        seed = 1
        classifier_name = classifier
        feature_extraction = None
        n_concurrent_jobs = 1
        chooser_module = ""
        n_initial_candidates = 0
    
    mypath = '../Candidates'
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
#     print onlyfiles
    
    for c_file in onlyfiles:
        if '.dat_' in c_file:
            subject = c_file.split('_')[-1]
            optimization_type = int(c_file.split('_')[1])
            Job_Params.chooser_module = c_file.split('_')[2]    
            Job_Params.feature_extraction = c_file.split('_')[4].split('.')[0]
            
            cand_file = os.path.join(mypath, c_file)
            dataset = subject_dataset_dict[subject]
            Job_Params.dataset = dataset
#             if ((dataset == 'BCICIII3b' and Job_Params.feature_extraction == 'morlet' and optimization_type == 1) or 
#             (dataset == 'BCICIII3b' and Job_Params.feature_extraction == 'BP' and optimization_type == 2)):
                 
            with open(cand_file, 'r') as f:
                all_lines = f.readlines()
                for line in all_lines:
                    if line.split(' ')[1] == 'P':
                        continue
                    params = map(float, line.split(' ')[2:])
                    all_subjects_candidates_list = BO_BCI.generate_all_candidates(dataset, optimization_type)
             
                    config = Configuration_BCI.Configuration_BCI('BCI_Framework', dataset)
     
                    sp = spearmint_lite.spearmint_lite(Job_Params, all_subjects_candidates_list, config, optimization_type)
                    sp.run_job(params, subject)
                    
                    print(subject)
                    print( dataset)
                    print(Job_Params.chooser_module)
                    print params
#     
    