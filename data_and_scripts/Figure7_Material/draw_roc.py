"""
(c) 2015 by Daniel Seita

This will draw my ROC curves.



Example after pass=10

Our thresholds: 50,100,150,200,250,300,350,400,450
Total test cases: 6348
Note that # of (+) and (-) tests cases are 3660 and 2688, respectively.

numCases = 0,114,253,1142,1366,1637,1088,623,125,0

infoMatrix, where rows are (TP,TN,FP,FN), and first col is the one that picks 2s (+) *most* frequently:
3660 3612 3460 2908 2151 1265 538 97 6 
0 66 167 757 1366 2117 2478 2660 2686 
2688 2622 2521 1931 1322 571 210 28 2 
0 48 200 752 1509 2395 3122 3563 3654 

In fact, here, the first col corresonds to the estimator that picks (+), always.

Sum of each column, should be the same: 6348,6348,6348,6348,6348,6348,6348,6348,6348
Now divide with TP/(TP+FN) = TP/3660 and TN/(TN+FP) = TN/2688:

specif = 0,0.024554,0.062128,0.28162,0.50818,0.78757,0.92188,0.98958,0.99926
1-specif (x-coord) = 1,0.97545,0.93787,0.71838,0.49182,0.21243,0.078125,0.010417,0.00074404
recall (y-coord)   = 1,0.98689,0.94536,0.79454,0.58770,0.34563,0.14699,0.026503,0.0016393



Example after pass=100:

Our thresholds: 50,100,150,200,250,300,350,400,450
Total test cases: 6348
Note that # of (+) and (-) tests cases are 3660 and 2688, respectively.

numCases = 0,66,183,648,1089,1548,940,823,1051,0

infoMatrix, where rows are (TP,TN,FP,FN), and first col is the one that picks 2s (+) *most*
frequently (we only need 10% of the 500 samples to be (+)s, and here that always happened):
3660 3645 3583 3293 2773 1960 1400 864 178
0 51 172 530 1099 1834 2214 2501 2664
2688 2637 2516 2158 1589 854 474 187 24
0 15 77 367 887 1700 2260 2796 3482

Sum of each column, should be the same: 6348,6348,6348,6348,6348,6348,6348,6348,6348
Now divide with TP/(TP+FN) = TP/3660 and TN/(TN+FP) = TN/2688:

specif = 0,0.018973,0.063988,0.19717,0.40885,0.68229,0.82366,0.93043,0.99107
1-specif (x-coord) = 1,0.98103,0.93601,0.80283,0.59115,0.31771,0.17634,0.069568,0.0089286
recall (y-coord)   = 1,0.99590,0.97896,0.89973,0.75765,0.53552,0.38251,0.23607, 0.048634



After pass=1000:

Our thresholds: 50,100,150,200,250,300,350,400,450
Total test cases: 6348
Note that # of (+) and (-) tests cases are 3660 and 2688, respectively.

numCases = 41,143,246,505,1053,931,887,894,1648,0

infoMatrix, where rows are (TP,TN,FP,FN), and first col is the one that picks 2s (+) *most* frequently:
3645 3581 3484 3241 2746 2264 1777 1225 411
26 105 254 516 1074 1523 1923 2265 2584
2662 2583 2434 2172 1614 1165 765 423 104
15 79 176 419 914 1396 1883 2435 3249

Sum of each column, should be the same: 6348,6348,6348,6348,6348,6348,6348,6348,6348
Now divide with TP/(TP+FN) = TP/3660 and TN/(TN+FP) = TN/2688:

specif = 0.0096726,0.039063,0.094494,0.19196,0.39955,0.56659,0.71540,0.84263,0.96131
1-specif (x-coord) = 0.99033,0.96094,0.90551,0.80804,0.60045,0.43341,0.28460,0.15737,0.038690
recall (y-coord)   = 0.99590,0.97842,0.95191,0.88552,0.75027,0.61858,0.48552,0.33470,0.11230


AUCs:

10: 0.58924
100: 0.65741
1000: 0.63792
"""

import matplotlib.pyplot as plt
import numpy as np

# Note! The first of our nine estimators is like the one that picks (+) always. The last one is
# *almost* like the one that picks (-) always. x is 1-spec, y is recall
#xcoords010 = [1, 0.97545, 0.93787, 0.71838, 0.49182, 0.21243, 0.078125, 0.010417, 0.0007440]
#ycoords010 = [1, 0.98689, 0.94536, 0.79454, 0.58770, 0.34563, 0.14699,  0.026503, 0.0016393]
xcoords100 = [0.80283, 0.59115, 0.31771, 0.17634, 0.069568]
ycoords100 = [0.89973, 0.75765, 0.53552, 0.38251, 0.236070]

plt.figure()

# Don't forget the BIDMach data which fills in the ROC curves.
data_010 = np.loadtxt('roc_results_10.txt')
data_100 = np.loadtxt('roc_results_100.txt')
data_1k = np.loadtxt('roc_results_1000.txt')
plt.plot([i/100.0 for i in range(0,100+1)], data_010, 'b-', linewidth=4.0, label='10 Passes (AUC = 0.58924)')
plt.plot([i/100.0 for i in range(0,100+1)], data_100, 'r-', linewidth=4.0, label='100 Passes (AUC = 0.65741)')
#plt.plot([i/100.0 for i in range(0,100+1)], data_1k,  'y-', linewidth=4.0, label='1000 Passes (AUC = 0.63792)')

# If I want a scatter plot, use this, but it's easier to just have straight lines going through.
#plt.scatter(xcoords010, ycoords010, s=120, c='b', marker='o')
plt.scatter(xcoords100, ycoords100, s=200, c='r', marker='o')
#plt.plot(xcoords010, ycoords010, 'bo-', markersize=12, linewidth=2, label='10 Passes (AUC = 0.58924)')
#plt.plot(xcoords100, ycoords100, 'r*-', markersize=18, linewidth=2, label='100 Passes (AUC = 0.65741)')
#plt.plot(xcoords1k, ycoords1k, 'y^-', markersize=18, linewidth=2, label='1000 Passes')

# Finally, do the diagonal line.
plt.plot([0,1], [0,1], color='k', linestyle='-', linewidth=3)

# So 10% means we only need 10% of samples to be a 1 to estimate a 1, hence estimate 1 very often.
labels = ['40%', '50%', '60%', '70%', '80%']
for (i, (label, x, y)) in enumerate(zip(labels, xcoords100, ycoords100)):
    plt.annotate(label, xy=(x,y), xytext=(-25,15), textcoords='offset points', size='large')

plt.legend(loc='lower right', borderpad=1, scatterpoints=1)
plt.title('BIDMach ROC (Real MOOC)', fontsize='xx-large')
plt.xlabel('False Positive Rate', fontsize='x-large')
plt.xlim([0,1])
plt.ylabel('True Positive Rate', fontsize='x-large')
plt.ylim([0,1])
plt.savefig('test.png')

