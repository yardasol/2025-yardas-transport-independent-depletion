GRPS=('casmo8' 'casmo40')
CASES=(2)
INTEGRATORS=('predictor' 'cecm')
MODES=('full')
TIMESCALES=('minutes' 'hours' 'days' 'months')
for g in ${GRPS[@]}
do
  cd $g
  for case in ${CASES[@]}
  do
    for integrator in ${INTEGRATORS[@]}
    do
      for mode in ${MODES[@]}
      do
        for scale in ${TIMESCALES[@]}
        do
          JOBNAME="$case-$scale-$integrator-$mode"
          DIRNAME="runtime-case$JOBNAME"
          FILENAME="case$JOBNAME.sh"
          cd $DIRNAME
          bash $FILENAME
          cd ../
        done
      done
    done
  done
  cd ../
done
