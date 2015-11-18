"""
(c) 2015 by Daniel Seita

Test for accuracy with our BayesNet.scala on different levels of sparsity for synthetic mooc data.
"""

import matplotlib.pyplot as plt
import numpy as np

output_files = [
    "kldivtime_02b_10perc_01same.txt",
    "kldivtime_02b_10perc_02same.txt",
    "kldivtime_02b_10perc_05same.txt",
    "kldivtime_02b_10perc_10same.txt",
    "kldivtime_02b_10perc_20same.txt"
]

batch_size = 2 ## NOTE NOTE NOTE Change as needed!

times = []
kldivs = []

for (i,item) in enumerate(output_files):
    with open(item, 'r') as log_file:
        kls = []
        tms = []
        for line in log_file:
            line_split = line.split()
            if (len(line_split) >= 3 and line_split[2] == "KLDiv,"): # Argh I have a comma...
                kls.append(float(line_split[0]))
            elif (len(line_split) >= 4 and ("secs" in line_split[3])):
                further_split = line_split[3].split("=")
                tms.append(float(further_split[1].rstrip(",")))
        times.append(tms)
        kldivs.append(kls[1:]) # Ignore the first one!

assert len(times[0]) == len(kldivs[0])+1

# Now plot! Note that for times[i] we take all *but* the last element!
signals = ['r-', 'c-', 'y-', 'b-', 'k-']
legend_labels = ["m = 1", "m = 2", "m = 5", "m = 10", "m = 20"]
widths = [6.0, 3.0, 3.0, 3.0, 3.0]

plt.figure()
for i in range(len(output_files)):
    plt.plot(times[i][:-1], kldivs[i], signals[i], label=legend_labels[i], linewidth=widths[i])

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=1, handlelength=5, borderpad=0.75, labelspacing=1)
plt.title('Time vs. KL Tradeoff (10% Synthetic MOOC)', fontsize='xx-large')
plt.xlabel('Time (Seconds)', fontsize='x-large')
plt.xlim([0,50])
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.ylim([0.01, 0.2])
plt.yscale('log')
plt.savefig('test.png')
