#!/bin/bash
echo "run the 2.5% with updates"
cd m1_2
t2="$(time (jags runJagsExe))"
echo "run the 10% with updates"
cd ../m1_10
t10="$(time (jags runJagsExe))"

cd ../m1_30
echo "run the 30% with updates"
t30="$(time (jags runJagsExe))"

cd ../m1_60
echo "run the 60% update"
t60="$(time (jags runJagsExe))"

cd ../m1_100
echo "run the 100% update"
t100="$(time (jags runJagsExe))"
cd ../
echo "$t2 $t10 $t30 $t60 $t100" > ./log
