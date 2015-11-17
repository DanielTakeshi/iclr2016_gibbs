#!/bin/bash

cd m1
echo "run the m1 update"
t10="$(time (jags runJagsExe))"

echo "run the m5 with updates"
cd ../m5
t20="$(time (jags runJagsExe))"

echo "run the m10 randomly with updates"
cd ../m10
t22="$(time (jags runJagsExe))"


