import numpy as np
import matplotlib.pyplot as plt
import csv


with open('./50PercentFile/m1/divRes', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
kl_50_1 = x.astype(np.float)

with open('./50PercentFile/m5/divRes', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
kl_50_5 = x.astype(np.float)


with open('./50PercentFile/m10/divRes', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
kl_50_10 = x.astype(np.float)

with open('./25PercentFile/m1/kldiv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
kl_25_1 = x.astype(np.float)


with open('./25PercentFile/m5/kldiv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
kl_25_5 = x.astype(np.float)

with open('./25PercentFile/m10/kldiv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
kl_25_10 = x.astype(np.float)

################

plt.figure()
#signals = ['ro--', 'y^--', 'bs--', 'ro-', 'y^-', 'bs-']
signals = ['r-', 'y-', 'b-', 'r-', 'y-', 'b-']
#legend_labels = ["25%, m = 1", "25%, m = 5", "25%, m = 10", "50%, m = 1", "50%, m = 5", "50%, m = 10"]
legend_labels = ["m = 1", "m = 5", "m = 10"]
#data = [kl_25_1, kl_25_5, kl_25_10, kl_50_1, kl_50_5, kl_50_10]
data = [kl_50_1, kl_50_5, kl_50_10]
i = 0
for i in xrange(3):
    linewidth_num = 3
    plt.plot(data[i][:200], signals[i], label=legend_labels[i], linewidth=linewidth_num)

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=1)

plt.title('JAGS Performance (Koller)', fontsize='xx-large')
plt.yscale('log')
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.savefig('fig_kl_div_25_50_perc_jags.png')
#######################################################
# draw the convergence vs time
time_25_1 = np.zeros(200)
time_25_1[0] = 13.8
timeInterval = (60 + 19.6 - time_25_1[0]) / 200
for i in xrange(200):
    time_25_1[i] = time_25_1[0] + i * timeInterval
    
time_25_5 = np.zeros(200)
time_25_5[0] = 2 * 60 + 16.3
timeInterval = (60 * 8 + 15.9 - time_25_5[0]) / 200
for i in xrange(200):
    time_25_5[i] = time_25_5[0] + i * timeInterval
    
time_25_10 = np.zeros(200)
time_25_10[0] = 7 * 60 + 4.3
timeInterval = (60 * 19 + 20.1 - time_25_10[0]) / 200
for i in xrange(200):
    time_25_10[i] = time_25_10[0] + i * timeInterval
    
time_50_1 = np.zeros(2000)
time_50_1[0] = 6.87
timeInterval = (60 * 6 + 8.8 - time_50_1[0]) / 2000
for i in xrange(2000):
    time_50_1[i] = time_50_1[0] + i * timeInterval
    
time_50_5 = np.zeros(300)
time_50_5[0] = 38.5
timeInterval = (60 * 6 + 39.6 - time_50_5[0]) / 300
for i in xrange(300):
    time_50_5[i] = time_50_5[0] + i * timeInterval
    
time_50_10 = np.zeros(200)
time_50_10[0] = 60 * 1 + 19.8
timeInterval = (60 * 8 + 58.6 - time_50_10[0]) / 200
for i in xrange(200):
    time_50_10[i] = time_50_10[0] + i * timeInterval


################################
plt.figure()
#signals = ['ro--', 'y^--', 'bs--', 'ro-', 'y^-', 'bs-']
signals = ['r-', 'y-', 'b-', 'r-', 'y-', 'b-']
#legend_labels = ["25%, m = 1", "25%, m = 5", "25%, m = 10", "50%, m = 1", "50%, m = 5", "50%, m = 10"]
legend_labels = ["m = 1", "m = 5", "m = 10"]
#data = [kl_25_1, kl_25_5, kl_25_10, kl_50_1, kl_50_5, kl_50_10]
data = [kl_50_1, kl_50_5, kl_50_10]
#time = [time_25_1, time_25_5, time_25_10, time_50_1, time_50_5, time_50_10]
time = [time_50_1, time_50_5, time_50_10]
i = 0
for i in xrange(3):
    linewidth_num = 2
    
    plt.plot(time[i], data[i], signals[i], label=legend_labels[i], linewidth=linewidth_num)

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=1)
plt.title('Average KL and Time Tradeoff (Koller)', fontsize='xx-large')
plt.yscale('log')
plt.xlabel('Seconds', fontsize='x-large')
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.xlim(0, 300)
plt.ylim(1e-5, 0.1)
plt.savefig('fig_kl_div_25_50_perc_jags_time.png')
