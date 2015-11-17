#!/bin/bash
echo "run the 2.0% with updates"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_2_0/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_2_0/divRes
echo "run the 2.5% with updates"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_2_5/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_2_5/divRes
echo "run the 2.2% with updates"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_2_2/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_2_2/divRes
echo "run the 2.2mooc% with updates"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_2_2_mooc_sparse/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_2_2_mooc_sparse/divRes
echo "run the 5% with updates"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_5/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_5/divRes
echo "run the 10% with updates"
java ComputeLogLikelihood moocDag.txt moocState.txt ./m1_10/CODAchain1.txt cpt_convert 1 4367 200 > ./m1_10/divRes
