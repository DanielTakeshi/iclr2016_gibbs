"""
(c) 2015 by Daniel Seita

Now this is the same as the Figure2 script, except this works with Figure 6, i.e., with the MOOC
data that involves forward sampling, then doing KL divergences, etc. Notes:

- I used a random seed of 0 to generated the original cpt, which I then used to forward sample the
  data. Then I cleared out the data so that zeros (i.e., unknowns) were in the same locations as the
  original data, so we still have just barely over 2.2% of the data here.
- Then we will run BayesNet.scala on the cleared out, forward generated data.
- I am running it using 1000 Gibbs sampling iterations, but obviously I can't plot that many
  markers. Maybe if it's just a straight line but it converges fairly quickly after about 50
  iterations.
- NOTE! I am also doing something different with the random seeds. I am running BayesNet using
  random seeds of 0, and random seeds of something else (say 10000). The reason is that having a
  random seed of 0 will result in much lower KL divergences, and using SAME = 10 with a random seed
  of 10 is worse than SAME = 1 but a random seed of 0. But fortunately, SAME = 1 with a random seed
  of 10 is worse than SAME = 10 with a random seed of 10, so it seems fairest to just use the same
  random seed for all trials, but NOT have it as 0.
- Also, we should analyze the resulting cpt to see how many decimal points of accuracy we have,
  since that would give some nice "intuition" to readers. Or the average element-wise difference in
  the 1362-dimensional CPT.
- Batch size is 4367, the full data.
- Hmmm ... interestingly enough, SAME = 10 is actually *worse*. I don't know, maybe due to increased
  sparsity? (For the random seed of 0 case. AND the random seed of 10000.)
- Also point out that if we do keep the random seed of 0, then our SAME actually performs much
  better relatively (so what we show, which is NOT the random seed of 0, if that is good, we should
  say that we could have gotten even better if we had truly optimized).

EDIT 11/17/15 much of the above is not relevant any more.
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

# These contain the BIDMach outout that gets printed. First, delete everything but the raw data
# itself. Fortunately, the batch size corresponds to the full data since there's no testing set.
output_files = ["out_mooc_01same_10000seed.txt",
                "out_mooc_02same_10000seed.txt",
                "out_mooc_05same_10000seed.txt",
                "out_mooc_10same_10000seed.txt"]

# Ideally, I'll just call this once (and then comment out this whole for loop here).
for item in output_files:
    with open(item, 'r') as old_file, open(str('data_') + item,'w') as new_file:
        for line in old_file:
            line_split = line.split()
            if (len(line_split) >= 3 and line_split[2] == "KLDiv"):
                new_file.write(line_split[0] + "\n")

# Now the next step is to plot. Load the files, then repeat the process. Each file that we're
# loading (via np.loadtxt(...)) needs to be ONLY the data itself, just one number per line.
plt.figure()
signals = ['k-', 'r--', 'b--', 'y--', 'z--']
legend_labels = ["m = 1", "m = 2", "m = 5", "m = 10", "jags, m=1"]

# load the data from jags
with open('./jags_data', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
jags = x.astype(np.float)

data0 = np.loadtxt(str('data_') + output_files[0])
data1 = np.loadtxt(str('data_') + output_files[1])
data2 = np.loadtxt(str('data_') + output_files[2])
data3 = np.loadtxt(str('data_') + output_files[3])

num_plot = 300
plt.plot(data0[:num_plot], signals[0], label=legend_labels[0], linewidth=5.0)
plt.plot(data1[:num_plot], signals[1], label=legend_labels[1], linewidth=4.0, dashes=(20,5))
plt.plot(data2[:num_plot], signals[2], label=legend_labels[2], linewidth=4.0, dashes=(10,5))
plt.plot(data3[:num_plot], signals[3], label=legend_labels[3], linewidth=4.0, dashes=(5,5))
plt.plot(jags, signals[3], label=legend_labels[4], linewidth=4.0, dashes=(2,5))
# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=1, handlelength=5, borderpad=1, labelspacing=1)
plt.title('Average KL Divergence on MOOC Data', fontsize='xx-large')
plt.yscale('log')
plt.ylim([0.1,0.4])
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.yticks(np.arange(0.1, 1, 0.05))
# print plt.xaxis.get_ticklabels()
plt.savefig('fig_mooc_kl_div.png')

