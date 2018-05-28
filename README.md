# ParaTask-WorkStealing
# SOFTENG 751 Project 3 Group 22, 2018

## Project Brief

Parallel execution environments like ParaTask normally manage the tasks to be executed in one or multiple queues. For dynamic load balancing, these environments then often employ work stealing approaches, where a worker thread without tasks steals from the queues of busy worker threads. Investigate the different work stealing approaches and algorithms in literature. Important distinguishing points are: queue structures and organisation, victim selection, stolen chunk sizes etc. Implement your own work stealing algorithms in the ParaTask runtime and compare its performance to the built in algorithms using simple application benchmarks. 

## ParallelTask

Parallel Task (AKA ParaTask) is an ongoing project under the Parallel and Reconfigurable Computing (PARC) lab at the University of Auckland in New Zealand. Parallel Task proposes a programming environment, in which programs can be parallelized with minimal changes required to the sequential version of object-oriented applications. To this effect, Parallel Task offers a set of language constructs that facilitate the setting up and configuration of asynchronous tasks. The language constructs thereof are proposed in the form of extended Java keywords for the earlier version of Parallel Task, and are provided as annotations for the later generation of Parallel Task. 
For more information abobut the projects that are currently being studied by PARC group please visit our website at: http://parallel.auckland.ac.nz/ParallelIT/ 

## Project Goal

Currently, in the ParaTask project, the work-stealing queue is implemented in the following way:

* Each worker thread maintains a local work queue in the form of a LinkedBlockingDeque<E> structure. New elements are added to and removed from the head of the queue (indicated by “first” in the LinkedBlockingDeque structure) using a last in first out (LIFO) policy, and are stolen by other worker thread from the tail (indicated by “last” in the LinkedBlockingDeque structure) using a first in first out (FIFO) policy.
* LIFO end: elements are (1) assigned from the global queue to the local work queues, and (2) popped by the work queues’ owner threads, from the same end of the deque. As such, the earlier the elements are assigned, the deeper they are stored, and the later they are accessed by the owner thread.
* FIFO end: elements are stolen by other threads from the opposite end from which they are added. In the stolen end, the earlier the elements are added, the earlier they are accessed by the thief thread.

This project aims to implement a circular blocking deque to replace the original one, which can grow when the deque is full. Local work deques in current ParaTask project are initialized with the size of max value of int, and they can be initialized with a smaller size when using a dynamic circular deque. The efficiency of the two work-stealing queue structures would be compared.


## Group Members
| Name                  | Github Username                                    | 
| --------------------- | -------------------------------------------------- |
| Michael Ieti          | [@michaelieti](https://github.com/michaelieti)     |
| Guolong (Peter) Kang  | [@kangguolong](https://github.com/kangguolong)     |
| Sha Luo               | [@ls-morning](https://github.com/ls-morning)       |

## How to run 

To run the project:  

First run the run.py script under the Linux environment(linux supports python automatically) using command "python3 run.py". Then the result folder will be regenerated. Note that the script will take several hours to run. So, be patient.  

To plot the result, run the plotting.py under the Linux environment suppose you have installed NumPy, matplotlib and pandas. Using command "python3 plotting.py". Then the plot folder will be regenerated and you will get the plot.svg under this folder.  

## Note
plotting.py depends on NumPy, matplotlib and pandas. So if you want to run this script to get the plotting result. Please make sure these dependencies have been installed.

It's better to backup the result folder and plot folder because run.py will regenerate result folder and plotting.py will regenerate plot folder.
