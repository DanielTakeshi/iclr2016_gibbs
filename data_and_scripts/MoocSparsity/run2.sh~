#!/bin/bash
echo "run the 2.2% with updates"
cd m1_2_2
t2="$(time (jags runJagsExe))"
echo "run the 2.5% with updates"
cd ../m1_2_5
t10="$(time (jags runJagsExe))"

cd ../m1_5
echo "run the 5% with updates"
t30="$(time (jags runJagsExe))"

cd ..
