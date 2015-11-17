#!/bin/bash
echo "run the 2.2% with updates"
cd m1_2_2_mooc_sparse
t2="$(time (jags runJagsExe))"

cd ../m1_5
echo "run the 5% with updates"
t30="$(time (jags runJagsExe))"

cd ../m1_10
echo "run the 10% with updates"
t30="$(time (jags runJagsExe))"

cd ../m1_25
echo "run the 25% with updates"
t30="$(time (jags runJagsExe))"

cd ..
