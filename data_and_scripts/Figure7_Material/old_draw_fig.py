"""
(c) 2015 by Daniel Seita

This will draw the predicton accuracy plot. I think this should be pretty straightforward, compared
to our other plots. The relevant lines are of the form

Accuracy: 0.5600189 = 3555.0 / 6348. Total 0/1 predicted = 2685,3663.

So just split it, check if the line has at least two components and starts with 'Accuracy', then
take the value at index 1 of the line split.

You know, we really don't need to bother with trying to generate the files that contain only the
data. It honestly makes things a bit more complicated/cluttered in the code repository.

It looks like I may have two plots, but each consists of three data points, so perhaps we will have
error bars here?
"""

import matplotlib.pyplot as plt
import numpy as np

same1 = [
    "pred_acc_seed0_gpubutgamma_200iter_1same.txt",
    "pred_acc_seed1337_gpubutgamma_200iter_1same.txt",
    "pred_acc_seed9999_gpubutgamma_200iter_1same.txt"
]
same5 = [
    "pred_acc_seed0_gpubutgamma_200iter_5same.txt",
    "pred_acc_seed1337_gpubutgamma_200iter_5same.txt",
    "pred_acc_seed9999_gpubutgamma_200iter_5same.txt"
]

a = []
for item in same1:
    with open(item, 'r') as datafile:
        b = []
        for line in datafile:
            line_split = line.split()
            if (len(line_split) >= 2 and line_split[0] == "Accuracy:"):
                b.append(float(line_split[1]))
    a.append(b)
a2 = []
for item in same5:
    with open(item, 'r') as datafile:
        b2 = []
        for line in datafile:
            line_split = line.split()
            if (len(line_split) >= 2 and line_split[0] == "Accuracy:"):
                b2.append(float(line_split[1]))
    a2.append(b2)

same1_np = np.array(a)
same1_mean = np.mean(same1_np, axis=0)
same1_std = np.std(same1_np, axis=0)
same5_np = np.array(a2)
same5_mean = np.mean(same5_np, axis=0)
same5_std = np.std(same5_np, axis=0)

plt.figure()
#plt.errorbar(np.arange(200), same1_mean, yerr=same1_std, fmt='k-', errorevery=5, linewidth=3, label="m = 1")
#plt.errorbar(np.arange(200), same5_mean, yerr=same5_std, fmt='y-', errorevery=5, linewidth=3, label="m = 5")
plt.plot(np.arange(200), same1_mean, 'k-', linewidth=5, label="m = 1")
plt.plot(np.arange(200), same5_mean, 'y-', linewidth=3, label="m = 5")
plt.legend(loc='lower right', ncol=1, handlelength=5, labelspacing=1)
plt.title('Prediction Accuracy (MOOC)', fontsize='xx-large')
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylim([0.53, 0.63])
plt.ylabel('Prediction Accuracy', fontsize='x-large')
plt.savefig('fig_prediction_accuracy_mooc.png')

