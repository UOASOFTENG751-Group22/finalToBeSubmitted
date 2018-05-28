#! /usr/bin/python3
import os
from shutil import rmtree
import subprocess

""" initialize variables """
problem_sizes = [2000, 4000, 6000, 8000, 10000]
iterations = 3
# problem_sizes = [20, 30, 40, 50]
resultFolder = "result"
resultFileName = "data_set.csv"
execution_kinds = ['Sequential', 'ParaTask', 'Modified_ParaTask']

benchmark_java_file = "uoa.se751.group22.benchmark.Benchmark"
ParaTask = "./ParaTask-Original.jar"
ParaTask_Modified = "./ParaTask-WorkStealingRuntime-1.0.1.jar"

""" delete exist result folder"""
if os.path.exists(resultFolder):
	rmtree(resultFolder)

""" create result folder"""
os.mkdir(resultFolder)

""" generate data function"""
def generate_data(file):
	for problem_size in problem_sizes:
		write_result(file, problem_size)

""" write result to data_set.csv file"""
def write_result(file, problem_size):
	for i in range(iterations + 1):
		exe_cmd_seq = "java -Xms1024M -Xmx6144M -cp .:%s:ParaTask-BenchmarkRuntime-1.0.0.jar %s SEQUENTIAL %d" %(ParaTask, benchmark_java_file, problem_size)
		exe_time_seq = subprocess.check_output(exe_cmd_seq, shell=True).decode('utf-8').strip('\r\n')
		file.write(execution_kinds[0] + "," + str(problem_size) + "," + str(exe_time_seq) + "\n")

		exe_cmd_para = "java -Xms1024M -Xmx6144M -cp .:%s:ParaTask-BenchmarkRuntime-1.0.0.jar %s STEAL %d" %(ParaTask, benchmark_java_file, problem_size)
		exe_time_para = subprocess.check_output(exe_cmd_para, shell=True).decode('utf-8').strip('\r\n')
		file.write(execution_kinds[1] + "," + str(problem_size) + "," + str(exe_time_para) + "\n")

		exe_cmd_para_modified = "java -Xms1024M -Xmx6144M -cp .:%s:ParaTask-BenchmarkRuntime-1.0.0.jar %s STEAL %d" %(ParaTask_Modified, benchmark_java_file, problem_size)
		exe_time_para_modified = subprocess.check_output(exe_cmd_para_modified, shell=True).decode('utf-8').strip('\r\n')
		file.write(execution_kinds[2] + "," + str(problem_size) + "," + str(exe_time_para_modified) + "\n")

""" open data_set.csv file and write result"""
print("start running.....")
with open(resultFolder + "/" + resultFileName, "w") as file:
	file.write("Execution_Kind,Problem_Size,Exe_Time\n")
	generate_data(file)
	
print("finished generating data finally!")
