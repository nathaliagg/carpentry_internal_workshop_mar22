#!/usr/bin/env python

################
# N. Graf-Grachet
# script for carpentry internal workshop Mar 22
# ANOVA and Tukey's test on pecan data and plotting figures
# ./stats_plotting.py
################

# always import packages first
import pandas as pd
import matplotlib as mpl 
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

# import data
pecan_data = pd.read_csv('data/Smith_pecan_data.csv', na_values='.')

# drop missing data
filtered_pecan_data = pecan_data.dropna()

# write a report file 
report_file = open('statistics_report.txt', 'w')

# obtain statistics and write to file
groupby_nrate = filtered_pecan_data.groupby('n_rate')

report_file.write("Nathalia's redemption..."+'\n'+'\n')

F1, p1 = stats.f_oneway(filtered_pecan_data['yield'], filtered_pecan_data['n_rate'])
mc = MultiComparison(filtered_pecan_data['yield'], filtered_pecan_data['n_rate'])
result1 = mc.tukeyhsd()
symb='-'
report_file.write('Effect of rate of N application on pecan yield'+'\n')
report_file.write('One-way ANOVA'+'\n')
report_file.write(symb*20+'\n')
report_file.write('F value:'+str(F1)+'\n')
report_file.write('P value:'+str(p1)+'\n')
report_file.write(symb*20+'\n')
report_file.write(str(result1)+'\n')
report_file.write('\n'+'\n'+'\n'+'\n')
print('Wrote statistics -- Effect of N on yield')

F2, p2 = stats.f_oneway(filtered_pecan_data['july'], filtered_pecan_data['n_rate'])
mc = MultiComparison(filtered_pecan_data['july'], filtered_pecan_data['n_rate'])
result2 = mc.tukeyhsd()
report_file.write('Effect of rate of N application on N content of leaves in July'+'\n')
report_file.write('One-way ANOVA'+'\n')
report_file.write(symb*20+'\n')
report_file.write('F value:'+str(F2)+'\n')
report_file.write('P value:'+str(p2)+'\n')
report_file.write(symb*20+'\n')
report_file.write(str(result2)+'\n')
report_file.write('\n'+'\n'+'\n'+'\n')
print('Wrote statistics -- Effect of rate of N application on N content of leaves in July')

F3, p3 = stats.f_oneway(filtered_pecan_data['oct'], filtered_pecan_data['n_rate'])
mc = MultiComparison(filtered_pecan_data['oct'], filtered_pecan_data['n_rate'])
result3 = mc.tukeyhsd()
report_file.write('Effect of rate of N application on N content of leaves in October'+'\n')
report_file.write('One-way ANOVA'+'\n')
report_file.write(symb*20+'\n')
report_file.write('F value:'+str(F3)+'\n')
report_file.write('P value:'+str(p3)+'\n')
report_file.write(symb*20+'\n')
report_file.write(str(result3)+'\n')
report_file.write('\n'+'\n'+'\n'+'\n')
print('Wrote statistics -- Effect of rate of N application on N content of leaves in October')

# plotting data

# boxplot
data_to_boxplot = pd.DataFrame({'n_rate': filtered_pecan_data['n_rate'].unique(), 'yield': filtered_pecan_data.groupby('n_rate')['yield'].mean()})

fig1 = plt.figure(1, figsize=(10, 7)) # setting plot dimensions
ax = fig1.add_subplot(111) # create axes
ax.set_title('Effect of rate of N application, in urea form, on pecan yield', fontsize=14) # set title
bx = ax.boxplot(data_to_boxplot) # plot data
ax.set_xlabel('N rates in %', fontsize=14) # x label
ax.set_ylabel('Pecan yield in kg/tree', fontsize=14) # y label
ax.set_yticks(np.arange(0, 46, 5)) # set y ticks 
ax.set_xticklabels(np.arange(0,0.9,0.2)) # set x ticklabels
fig1.savefig('from_script_boxplot_N_yield.png', bbox_inches='tight')

print('Saved boxplot as .png figure')

# barplot
N=5
ind = np.arange(N) # for x axis

#setting data means and std
july_mean = filtered_pecan_data['july'].mean()
july_std = filtered_pecan_data['july'].std()
oct_mean = filtered_pecan_data['oct'].mean()
oct_std = filtered_pecan_data['oct'].std()

fig2 = plt.figure(2, figsize=(8, 7))
width=0.4 # of the bar
fig2 = plt.bar(ind, july_mean, width, yerr=july_std, color='cornflowerblue')
fig2 = plt.bar(ind, oct_mean, width, yerr=oct_std, color='hotpink')
plt.ylabel('% dry weight of N', fontsize=14)
plt.title('N content of pecan leaves in July and October', fontsize=14)
plt.xticks(ind, ('0', '0.2', '0.4', '0.6', '0.8'))
plt.xlabel('N rates in %', fontsize=14)
plt.yticks(np.arange(0, 3.1, 0.5))
plt.legend(('July', 'October'), loc=4, ncol=2, framealpha=1)
fig2 = plt.savefig('from_script_barplot_Ncontent_months.png', bbox_inches='tight')

print('Saved barplot as .png figure')

print('DONE!!')
report_file.close()
