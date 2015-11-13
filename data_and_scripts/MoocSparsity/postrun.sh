#!/bin/bash
echo "run the 2.5% with updates"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_2/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_2/divRes

echo "run the 10% with updates"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_10/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_10/divRes

echo "run the 30% with updates"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_30/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_30/divRes

echo "run the 60% update"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_60/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_60/divRes

echo "run the 100% update"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_100/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_100/divRes
