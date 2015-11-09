#!/bin/bash
echo "run the m = 1 with no updates"
cd m1
time jags runJagsExe_noUpdate
echo "run the m = 1 with 200"
time jags runJagsExe

cd ../m5
echo "run the m = 5 with no updates"
time jags runJagsExe_noUpdate
echo "run the m = 5 200 update"
time jags runJagsExe

echo "run the m = 10 with no updates"
cd ../m10
time jags runJagsExe_noUpdate
echo "run the m = 10 with 200 update"
time jags runJagsExe
cd ../
