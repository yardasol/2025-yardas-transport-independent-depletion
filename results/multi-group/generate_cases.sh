GRPS=('casmo8' 'casmo40')
CASES=(2)
INTEGRATORS=('predictor' 'cecm')
MODES=('simple' 'full')
TIMESCALES=('minutes' 'hours' 'days' 'months')
for group in ${GRPS[@]}
do
  for case in ${CASES[@]}
  do
    mkdir -p $group/case$case
    for integrator in ${INTEGRATORS[@]}
    do
      mkdir -p $group/case$case/$integrator
      for mode in ${MODES[@]}
      do
        for scale in ${TIMESCALES[@]}
        do
          JOBNAME="$case-$scale-$integrator-$mode"
          DIRNAME="$group/runtime-case$JOBNAME"
          FILENAME=$DIRNAME"/case$JOBNAME.sh"
          mkdir -p $DIRNAME
          touch $FILENAME
          echo "python ../../run_depletion_case.py -g $group -c $case -i $integrator -m $mode -t $scale" > $FILENAME
        done
      done
    done
  done
done
