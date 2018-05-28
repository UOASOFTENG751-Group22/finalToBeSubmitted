# -*- coding: utf-8 -*-
import os
from shutil import rmtree
from pandas import DataFrame
import matplotlib.pyplot as plt
import pandas as pd
import glob

problem_sizes = [2000, 4000, 60000, 8000, 10000]
data_source_path = './result/'
plot_folder = './plot'

frame = DataFrame()
source_list = []
for data_source in glob.glob(data_source_path + '*.csv'):
    data_set = pd.read_csv(data_source)
    source_list.append(data_set)
    
if os.path.exists(plot_folder):
	rmtree(plot_folder)
os.mkdir(plot_folder)

frame = pd.concat(source_list)

grouped = frame['Exe_Time'].groupby([frame['Execution_Kind'], frame['Problem_Size']])
mean_ds = grouped.mean().reset_index()
exe_time_plot = pd.pivot_table(mean_ds, index='Problem_Size', columns ='Execution_Kind')
fig = plt.figure()
fig.set_size_inches(14, 7.5)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
chart = fig.add_subplot(2, 1, 1)
chart.set_title('Execution time with increasing problem size')
chart.set_xlabel('Problem_Size')
chart.set_ylabel('Execution Time (ms)')
plt.plot(exe_time_plot, 'o-')
plt.legend(('Modified_ParaTask','ParaTask','Sequential'), loc='best')


filtered_dataset = []
filtered_frame = DataFrame()
for problemSize in problem_sizes:
    seq_time = mean_ds.loc[(mean_ds['Execution_Kind']=='Sequential') & (mean_ds['Problem_Size'] == problemSize),'Exe_Time']
    parallel_ds = mean_ds.loc[(mean_ds['Execution_Kind']!='Sequential') & (mean_ds['Problem_Size'] == problemSize)]
    parallel_ds['Speedup'] = seq_time.values[0]/parallel_ds.Exe_Time
    filtered_dataset.append(parallel_ds)

filtered_frame = pd.concat(filtered_dataset)
filtered_frame = filtered_frame.drop(['Exe_Time'], axis=1)
speedup_plot = pd.pivot_table(filtered_frame, index='Problem_Size', columns ='Execution_Kind')
speedup_chart = fig.add_subplot(2, 1, 2)
speedup_chart.set_title('speedup with increasing problem size')
speedup_chart.set_xlabel('Problem_Size')
speedup_chart.set_ylabel('Speedup')
plt.plot(speedup_plot, 'o-')
plt.legend(('Modified_ParaTask','ParaTask'), loc='best')
plt.savefig(plot_folder + '/analysis.svg', dpi=400, bbox_inches='tight')

    