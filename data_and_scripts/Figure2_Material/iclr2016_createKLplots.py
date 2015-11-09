"""
(c) 2015 by Daniel Seita

This will automatically create the plots that I need. That way, I avoid tedious micromanagement.
Here's how to use it. Run

./sbt package; ./bidmach scripts/bn_sest.ssc > out.txt

with different SAME values (or different data) each time, and make sure the output file is of a
correct/known form. (We can't use subprocess because we have to modfiy the actual BIDMach code ...
ugh.) Make sure I put the file names in the "output_files" list below. Then just run everything. It
should parse the data and only keep the KL divergence stuff. Then we take the *average* of the KL
divergences across all the *test-set* mini-batches.

I'm currently using a batch size of 25,000 because stout has really bad GPUs.
"""

import matplotlib.pyplot as plt
import numpy as np

# These contain the BIDMach outout that gets printed. First, delete everything but the raw data
# itself. Also, that raw data needs to have the AVERAGE of the KL divergences across *all*
# mini-batches, not just the ones that are "testing" (b/c no notion of testing here, really).
output_files = [
                "out_student50_seed0_same01_gpu.txt",
                "out_student50_seed0_same05_gpu.txt",
                "out_student50_seed0_same10_gpu.txt",
                "out_student50_seed0_same01.txt",
                "out_student50_seed0_same05.txt",
                "out_student50_seed0_same10.txt"
                ]

# Note: ideally, I'll just call this once (and then comment out this whole for loop here).
for item in output_files:
    with open(item, 'r') as old_file, open(str('data_') + item,'w') as new_file:
        for line in old_file:
            line_split = line.split()
            if (len(line_split) >= 3 and line_split[2] == "KLDiv"):
                new_file.write(line_split[0] + "\n")

# Now the next step is to plot. Load the files, then repeat the process. Each file that we're
# loading into this array needs to be ONLY the data itself, just one number per line. Nothing more!
plt.figure()
signals = ['r--', 'y--', 'b--', 'r-', 'y-', 'b-']
legend_labels = [
    "50%, m = 1",
    "50%, m = 5",
    "50%, m = 10",
    "50%, m = 1", 
    "50%, m = 5",
    "50%, m = 10"
    ]

i = 0
for item in output_files:
    data = np.loadtxt(str('data_') + item)
    linewidth_num = 1.5
    if i >= 3:
        linewidth_num = 3.0
    plt.plot(data[:100], signals[i], label=legend_labels[i], linewidth=linewidth_num)
    i += 1

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=2)
plt.title('Average KL Divergence on Student Data', fontsize='xx-large')
plt.yscale('log')
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.savefig('fig_kl_div_25_50_perc.png')

