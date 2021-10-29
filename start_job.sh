# Launch the MapReduce Job

while getopts "f:" opt; do
  case ${opt} in
    f ) # process option f
      cat $OPTARG | python map.py | python sort.py | python groupByKey.py | python reduceByKey.py
      ;;
    \? ) echo "Usage: cmd [-f]"
      ;;
  esac
done
