import numpy as np
import matplotlib.pyplot as plt
import csv

with open('./m1_2_2_mooc_sparse/divRes', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
m1_2_2_mooc = x.astype(np.float)

with open('./m1_5/divRes', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
m1_5 = x.astype(np.float)

with open('./m1_10/divRes', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
m1_10 = x.astype(np.float)

with open('./m1_25/divRes', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
m1_25 = x.astype(np.float)


################

plt.figure()
#signals = ['ro--', 'y^--', 'bs--', 'ro-', 'y^-', 'bs-']
signals = ['r-', 'y-', 'b-', 'k-', 'y-', 'y--', 'c-', 'c--']
#legend_labels = ["25%, m = 1", "25%, m = 5", "25%, m = 10", "50%, m = 1", "50%, m = 5", "50%, m = 10"]
legend_labels = ["2.2% known", "5% known", "10% known", "25% known"]
#data = [kl_25_1, kl_25_5, kl_25_10, kl_50_1, kl_50_5, kl_50_10]
data = [m1_2_2_mooc, m1_5, m1_10, m1_25]
i = 0
for i in xrange(4):
    linewidth_num = 3
    plt.plot(data[i][:300], signals[i], label=legend_labels[i], linewidth=linewidth_num)

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=2)
plt.title('JAGS Performance (Synthetic Mooc)', fontsize='xx-large')
plt.yscale('log')
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.savefig('fig_diff_sparsity_jags.png')
#######################################################

