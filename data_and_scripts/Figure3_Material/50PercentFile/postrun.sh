#!/bin/bash
echo "run the m1 with updates"
java ComputeLogLikelihood dag state ./m1/CODAchain1.txt cpt 1 50000 200 > ./m1/divRes

echo "run the m5 with updates"
java ComputeLogLikelihood dag state ./m5/CODAchain1.txt cpt 5 50000 200 > ./m5/divRes

echo "run the m10 with updates"
java ComputeLogLikelihood dag state ./m10/CODAchain1.txt cpt 10 50000 200 > ./m10/divRes

