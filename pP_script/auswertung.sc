#!/bin/bash

#rm log*
rm /system/sampleDict_python_plotlines
#mkdir Auswertungsdaten
cd ..
#postProcess -func Lambda2
#postProcess -func sampleDict_plane_U

cp pP_script/alleranfang.py postProcessing/
cd postProcessing
python3.6 alleranfang.py

cd ..
postProcess -func sampleDict_python_plotlines


cp pP_script/gnuplotpP.py postProcessing/
cd postProcessing
python3.6 gnuplotpP.py

rm gnuplotpP.py
rm alleranfang.py











## Copy mesh:
# cp -r /home.temp/fds159/feder/OpenFOAM/feder-1706/chow/meshing/snappy5_f/8/polyMesh/ constant/

## Execute with of v1706
# mapFields -consistent -sourceTime 4000 ../../snappy4_LEnoCyl_0.75/SST_simple
# rm -r processor*
# rm log.simpleFoam

#decomposePar -constant

## Don't do potiFoam, because the initial fields were mapped!!
# mpirun -np 4 potentialFoam -parallel -writep | tee log.potFoam
#mpirun -np 4 simpleFoam -parallel | tee log.simpleFoam

## Postprocessing with of1706?

#selber rausgemacht
#mpirun -np 10 vorticity -parallel -latestTime
#mpirun -np 10 Lambda2 -parallel -latestTime
#mpirun -np 10 yPlusRAS -parallel -latestTime | tee log.yPlus -a

#reconstructPar -latestTime

# cp system/sampleDict_plane_U system/sampleDict
# sample -time 300
