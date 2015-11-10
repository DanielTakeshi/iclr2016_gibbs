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
                "test_student_batch02_same01.txt",
                "test_student_batch02_same05.txt",
                "test_student_batch02_same10.txt"
                ]

# Note: ideally, I'll just call this once (and then comment out this whole for loop here).
i = 3
for item in output_files:
    with open(item, 'r') as old_file, open(str('data_') + item,'w') as new_file:
        kls = []
        for line in old_file:
            line_split = line.split()
            if (len(line_split) >= 3 and line_split[2] == "KLDiv"):
                if (i >= 3):
                    kls.append(float(line_split[0]))
                else:
                    new_file.write(line_split[0] + "\n")
        if (i >= 3):
            for k in range(0, len(kls), 2):
                kl = (kls[k] + kls[k+1])/2.0
                new_file.write(str(kl) + "\n")
    i += 1

# Now the next step is to plot. Load the files, then repeat the process. Each file that we're
# loading into this array needs to be ONLY the data itself, just one number per line. Nothing more!
plt.figure()
signals = ['r-', 'y-', 'b-', 'r-', 'y-', 'b-']
legend_labels = [
    "m = 1",
    "m = 5",
    "m = 10"
    ]

i = 0
for item in output_files:
    data = np.loadtxt(str('data_') + item)
    linewidth_num = 3.0
    if i >= 3:
        linewidth_num = 3.0
    plt.plot(data[:100], signals[i], label=legend_labels[i], linewidth=linewidth_num)
    i += 1

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=1)
plt.title('Average KL Divergence on Student Data', fontsize='xx-large')
plt.yscale('log')
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.savefig('TEST.png')

