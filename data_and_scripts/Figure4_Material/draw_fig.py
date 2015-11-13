"""
(c) 2015 by Daniel Seita

This will create the plots for Figure 4, showing the KL-time tradeoff for the 5-variable data.

To be honest, I am not sure if this is what we want to do...

Batch size: 25,000. Total data: 50,000.
"""

import matplotlib.pyplot as plt
import numpy as np

# These contain the BIDMach outout that gets printed. First, delete everything but the raw data
# itself. Also, that raw data needs to have the AVERAGE of the KL divergences across *all*
# mini-batches, not just the ones that are "testing" (b/c no notion of testing here, really).
output_files = [
     "kl_time_tradeoff_koller_01same_1337seed.txt",
     "kl_time_tradeoff_koller_05same_1337seed.txt",
     "kl_time_tradeoff_koller_10same_1337seed.txt"
]

kldiv = []
times = []

for (i,element) in enumerate(output_files):
    with open(element, 'r') as log_file:
        kls = []
        tms = []
        for line in log_file:
            line_split = line.split()
            if (len(line_split) >= 3 and line_split[2] == "KLDiv"):
                kls.append(float(line_split[0]))
            elif (len(line_split) >= 4 and ("secs" in line_split[3])):
                further_split = line_split[3].split("=")
                tms.append(float(further_split[1].rstrip(",")))
        kldiv.append( [(a+b)/2.0 for (a,b) in zip(kls[::2], kls[1::2])] ) # Avg every two elems
        times.append(tms)
assert len(kldiv) == len(output_files)

# Now plot!
signals = ['r-', 'y-', 'b-', 'c*-', 'm*-']
legend_labels = [
    "m = 1",
    "m = 5",
    "m = 10"
]

plt.figure()
for i in range(len(output_files)):
    plt.plot(times[i], kldiv[i], signals[i], label=legend_labels[i], linewidth=2.0)

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=1)
plt.title('Average KL and Time Tradeoff (Koller)', fontsize='xx-large')
plt.xlabel('Time (Seconds)', fontsize='x-large')
plt.xlim([0,10])
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.yscale('log')
plt.ylim([10**(-5),10**(-1)])
plt.savefig('kl_time_tradeoff_koller_data.png')
