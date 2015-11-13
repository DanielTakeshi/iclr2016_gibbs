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

accuracies_1 = []
with open("pred_acc_seed0_gpubutgamma_200iter_1same.txt", 'r') as data_file:
    for line in data_file:
        line_split = line.split()
        if (len(line_split) >= 2 and line_split[0] == "Accuracy:"):
            accuracies_1.append(float(line_split[1]))

accuracies_2 = []
with open("pred_acc_seed1337_gpubutgamma_200iter_1same.txt", 'r') as data_file:
    for line in data_file:
        line_split = line.split()
        if (len(line_split) >= 2 and line_split[0] == "Accuracy:"):
            accuracies_2.append(float(line_split[1]))

accuracies_3 = []
with open("pred_acc_seed9999_gpubutgamma_200iter_1same.txt", 'r') as data_file:
    for line in data_file:
        line_split = line.split()
        if (len(line_split) >= 2 and line_split[0] == "Accuracy:"):
            accuracies_3.append(float(line_split[1]))

plt.figure()
plt.plot(accuracies_1, 'r-', label="Seed 0000", linewidth = 3.0)
plt.plot(accuracies_2, 'y-', label="Seed 1337", linewidth = 3.0)
plt.plot(accuracies_3, 'b-', label="Seed 9999", linewidth = 3.0)
plt.legend(loc='lower right', ncol=1)
plt.title('Prediction Accuracy on MOOC Data', fontsize='xx-large')
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylabel('Prediction Accuracy', fontsize='x-large')
plt.savefig('fig_prediction_accuracy_mooc.png')

