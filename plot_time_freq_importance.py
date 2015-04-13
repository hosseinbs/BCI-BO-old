"""
Pyplot animation example.

The method shown here is only for very simple, low-performance
use.  For more demanding applications, look at the animation
module and the examples that use it.
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import sys
os.chdir('../bci_framework')
sys.path.append('./BCI_Framework')

import Main
import Configuration_BCI

import Single_Job_runner as SJR
import numpy as np
import itertools


dataset = 'BCICIII3b'
config = Configuration_BCI.Configuration_BCI('BCI_Framework', dataset)
feature = 'morlet'
morlet_y_length = 20
chooser_modules = ['GPEIOptChooser', 'RandomForestEIChooser', 'RandomChooser']
if feature == 'BP':
    f_type = 2
else:
    f_type = 1 
    
for subj_ind, subject in enumerate(config.configuration['subject_names_str']):
    
    fig, axes = plt.subplots(nrows=1, ncols=3)
    ax0, ax1, ax2 = axes.flat
    
    for chooser_module_ind, chooser_module in enumerate(chooser_modules):
        
        x = np.arange(config.configuration['movement_trial_size_list'][subj_ind])
        y = np.arange(620)
        
        if feature == 'BP':
            z = np.zeros((len(y),len(x)))
            sum_count = np.ones((len(y),len(x)))
        else:
            z = np.zeros((morlet_y_length,len(x)))
            sum_count = np.ones((morlet_y_length,len(x)))

         
        file_name = '../../Candidates/results_' + str(f_type) + '_' + chooser_module + '_LogisticRegression_'+ feature +'.dat_' + subject
        with open(os.path.join('BCI_Framework',file_name), 'r') as candidates_file:
            
            all_candidates = candidates_file.readlines()
    #     all_cands = np.loadtxt(os.path.join('BCI_Framework',file_name))
        for candidate in all_candidates:
            print candidate
            candidate = candidate.strip()
            if 'P' not in candidate:
                
                candidates_array = map(float, candidate.split())
                
                weight = candidates_array[0] * 100
                
                low_time = candidates_array[2]
                high_time = candidates_array[3]
                
                if feature == 'BP':
                    low_freq1 = 20*candidates_array[4]
                    high_freq1 = 20*candidates_array[5]
                
                    low_freq2 = 20*candidates_array[6]
                    high_freq2 = 20*candidates_array[7]
                    z[-high_freq1:-low_freq1, low_time:-high_time] += weight
                    sum_count[-high_freq1:-low_freq1, low_time:-high_time] += 1
                else:
                    z[0:, low_time:-high_time] += weight
                    sum_count[0:, low_time:-high_time] += 1
        
                
#                 z[-high_freq1:-low_freq1, low_time:-high_time] += weight
#                 z[-high_freq2:-low_freq2, low_time:-high_time] += weight
                 
        z = z/sum_count
    #     z = z * 100
        np.savetxt('z.csv', z, fmt='%.2f', delimiter = ',')
#         plt.subplot(3, chooser_module_ind + 1, 1)
        ax = axes.flat[chooser_module_ind]
        p = ax.imshow(z)
#         p = plt.imshow(z)
#         fig = ax.gcf()
#         ax.clim()   # clamp the color limits
        
        
        mv_length = config.configuration['movement_trial_size_list'][subj_ind]/float(config.configuration['sampling_rate'])
        tick_locs = np.arange(mv_length+1) * float(config.configuration['sampling_rate'])
        tick_lbls = np.arange(mv_length+1)
#         ax.set_xticklabels(tick_locs, tick_lbls)
        ax.set_xticks(tick_locs)
        ax.set_xticklabels([' '] + tick_lbls[1:].tolist())
        
#         tick_locs = np.arange(32) * 20
#         tick_lbls = list(reversed(range(32)))

#         ax.set_yticks(tick_locs)
#         
#         ax.set_yticklabels(tick_lbls[0:31] + [' '])
        ax.set_title(chooser_module, fontsize=18)
        ax.set_xlabel('Time (seconds)', fontsize=18)
        if chooser_module_ind == 0:
            ax.set_ylabel('Frequency (HZs)', fontsize=18)
#     plt.clim()
#     plt.title("Time/Frequency importance of the the signal")
    cax = fig.add_axes([0.91, 0.22, 0.03, 0.56])

    fig.colorbar(p,cax)
#     plt.colorbar()
    plt.show()


# p = plt.imshow(z)
# fig = plt.gcf()
# plt.clim()   # clamp the color limits
# plt.title("Boring slide show")
# 
# plt.show()

# for i in xrange(5):
#     if i==0:
#         p = plt.imshow(z)
#         fig = plt.gcf()
#         plt.clim()   # clamp the color limits
#         plt.title("Boring slide show")
#     else:
#         z = z + 2
#         p.set_data(z)
# 
#     print("step", i)
#     plt.pause(0.5)