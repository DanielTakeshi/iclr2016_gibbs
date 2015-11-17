"""
(c) 2015 by Daniel Seita

This will automatically create the plots that I need. That way, I avoid tedious micromanagement.
Here's how to use it. Run

./sbt package; ./bidmach scripts/bn_sest.ssc > out.txt

Then manage the out.txt files.
"""

import matplotlib.pyplot as plt
import numpy as np

# Don't forget to take the KL divergence of the NEXT pass, b/c that indicates the "end" of one pass.
# OK, let's do a batch size of 12.5k, I guess. :( It gets slightly better convergence behavior due
# to more updates.
output_files = [
    "koller_kldiv_gpu_same01_4mb.txt",
    "koller_kldiv_gpu_same05_4mb.txt",
    "koller_kldiv_gpu_same10_4mb.txt"
]
factor = 4 #### NOTE NOTE NOTE Be sure to change the factor accordingly!!! It should be 2 or 4...

data = []
for (i,item) in enumerate(output_files):
    with open(item, 'r') as log_file:
        kls = []
        for line in log_file:
            line_split = line.split()
            if (len(line_split) >= 3 and line_split[2] == "KLDiv"):
                kls.append(float(line_split[0]))
        data.append( kls[factor::factor] )  # E.g., if 2, then this is indices 2, 4, 6, etc.

# Now set up the plot.
plt.figure()
signals = ['r-', 'y-', 'b-']
legend_labels = [
    "m = 1",
    "m = 5",
    "m = 10",
]

plt.plot(data[0], signals[0], label=legend_labels[0], linewidth=3.0)
plt.plot(data[1], signals[1], label=legend_labels[1], linewidth=3.0)
plt.plot(data[2], signals[2], label=legend_labels[2], linewidth=3.0)

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=1)
plt.title('BIDMach Performance (Koller)', fontsize='xx-large')
plt.yscale('log')
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.savefig('fig_kldiv_koller_mb4_gpu.png')

