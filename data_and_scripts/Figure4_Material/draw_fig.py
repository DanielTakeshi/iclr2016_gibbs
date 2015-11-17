"""
(c) 2015 by Daniel Seita

Test for accuracy with our BayesNet.scala on different levels of sparsity for synthetic mooc data.
"""

import matplotlib.pyplot as plt
import numpy as np

output_files = [
    "kldiv_synthmooc022_matchsparsity_02b_500iter.txt",
    "kldiv_synthmooc050_02b_500iter.txt",
    "kldiv_synthmooc100_02b_500iter.txt",
    "kldiv_synthmooc250_02b_500iter.txt"
]

factor = 2 ## NOTE NOTE NOTE Change as needed!

data = []
for (i,item) in enumerate(output_files):
    with open(item, 'r') as log_file:
        kls = []
        for line in log_file:
            line_split = line.split()
            if (len(line_split) >= 3 and line_split[2] == "KLDiv"):
                kls.append(float(line_split[0]))
        data.append(kls[factor::factor]) 

# Now plot!
signals = ['r-', 'y-', 'b-', 'k-']
legend_labels = ["2.2% known", "5% known", "10% known", "25% known"]

plt.figure()
for i in range(len(output_files)):
    plt.plot(data[i][:500], signals[i], label=legend_labels[i], linewidth=3.0)

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=1)
plt.title('BIDMach Performance (Synthetic MOOC)', fontsize='xx-large')
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.yscale('log')
plt.savefig('test.png')
