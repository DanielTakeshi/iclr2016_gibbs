import numpy as np
import matplotlib.pyplot as plt
import csv


with open('./50PercentFile/m1_long/kldiv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
kl_50_1 = x.astype(np.float)

with open('./50PercentFile/m5/kldiv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        x = row
x = np.array(x)
kl_50_5 = x.astype(np.float)


with open('./50PercentFile/m10/kldiv', 'rb') as csvfile:
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
signals = ['r-', 'y-', 'b-']
#legend_labels = ["25%, m = 1", "25%, m = 5", "25%, m = 10", "50%, m = 1", "50%, m = 5", "50%, m = 10"]
legend_labels = ["m = 1", "m = 5", "m = 10"]
#data = [kl_25_1, kl_25_5, kl_25_10, kl_50_1, kl_50_5, kl_50_10]
data = [kl_50_1, kl_50_5, kl_50_10]
i = 0
for i in xrange(3):
    linewidth_num = 3
    plt.plot(data[i][:100], signals[i], label=legend_labels[i], linewidth=linewidth_num)

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=2)
plt.title('Average KL Divergence on Student Data', fontsize='xx-large')
plt.yscale('log')
plt.xlabel('Number of Passes Over the Data', fontsize='x-large')
plt.ylabel('Average KL Divergence', fontsize='x-large')
plt.savefig('fig_kl_div_25_50_perc.png')
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
time_50_1[0] = 9.7
timeInterval = (60 * 11 + 52.6 - time_50_1[0]) / 200
for i in xrange(2000):
    time_50_1[i] = time_50_1[0] + i * timeInterval
    
time_50_5 = np.zeros(200)
time_50_5[0] = 60 + 28.6
timeInterval = (60 * 7 + 57.0 - time_50_5[0]) / 200
for i in xrange(200):
    time_50_5[i] = time_50_5[0] + i * timeInterval
    
time_50_10 = np.zeros(200)
time_50_10[0] = 60 * 4 + 27.1
timeInterval = (60 * 17 + 21.4 - time_50_10[0]) / 200
for i in xrange(200):
    time_50_10[i] = time_50_10[0] + i * timeInterval


################################
plt.figure()
#signals = ['ro--', 'y^--', 'bs--', 'ro-', 'y^-', 'bs-']
signals = ['r-', 'y-', 'b-']
#legend_labels = ["25%, m = 1", "25%, m = 5", "25%, m = 10", "50%, m = 1", "50%, m = 5", "50%, m = 10"]
legend_labels = ["m = 1", "m = 5", "m = 10"]
#data = [kl_25_1, kl_25_5, kl_25_10, kl_50_1, kl_50_5, kl_50_10]
data = [kl_50_1, kl_50_5, kl_50_10]
#time = [time_25_1, time_25_5, time_25_10, time_50_1, time_50_5, time_50_10]
time = [time_50_1, time_50_5, time_50_10]
i = 0
for i in xrange(3):
    linewidth_num = 3
    
    plt.plot(time[i], data[i], label=legend_labels[i], linewidth=linewidth_num)

# Be sure to increase the font sizes! I might also have to experiment with a lot of other settings.
plt.legend(loc='upper right', ncol=2)
plt.title('Convergence Based on Seconds', fontsize='xx-large')
plt.yscale('log')
plt.xlabel('Seconds', fontsize='x-large')
plt.ylabel('(Log)Average KL Divergence', fontsize='x-large')
plt.xlim(0, 400)
plt.savefig('fig_kl_div_25_50_perc_jags_time.png')
