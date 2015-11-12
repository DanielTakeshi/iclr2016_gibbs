"""
(c) 2015 by Daniel Seita

This will draw the predicton accuracy plot. I think this should be pretty straightforward, compared
to our other plots. The relevant lines are of the form

Accuracy: 0.5600189 = 3555.0 / 6348. Total 0/1 predicted = 2685,3663.

So just split it, check if the line has at least two components and starts with 'Accuracy', then
take the value at index 1 of the line split.

You know, we really don't need to bother with trying to generate the files that contain only the
data. It honestly makes things a bit more complicated/cluttered in the code repository.

Note: this is a draft at the moment. I don't think we'll have one CPU and one GPU plot ...
"""

import matplotlib.pyplot as plt
import numpy as np

# CPU Gamma Random Number Generation
accuracies_cpu = []
with open("prediction_accuracy_mooc_100iter_cpu.txt", 'r') as data_file:
    for line in data_file:
        line_split = line.split()
        if (len(line_split) >= 2 and line_split[0] == "Accuracy:"):
            accuracies_cpu.append(float(line_split[1]))

# GPU Gamma Random Number Generation
accuracies_gpu = []
with open("prediction_accuracy_mooc_100iter_gpu.txt", 'r') as data_file:
    for line in data_file:
        line_split = line.split()
        if (len(line_split) >= 2 and line_split[0] == "Accuracy:"):
            accuracies_gpu.append(float(line_split[1]))

plt.figure()
plt.plot(accuracies_cpu, 'r-', label="CPU Gamma", linewidth = 3.0) # CPU
plt.plot(accuracies_gpu, 'b-', label="GPU Gamma", linewidth = 3.0) # GPU
plt.legend(loc='lower right', ncol=1)
plt.title('Prediction Accuracy on MOOC Data', fontsize='xx-large')
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylabel('Prediction Accuracy', fontsize='x-large')
plt.savefig('fig_prediction_accuracy_mooc.png')

