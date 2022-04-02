while getopts f:e: opt
do
  case $opt in
  f)
  opts=`more "$OPTARG"`
  python bfr.py "$opts"
  ;;
  e)
  python bfr.py "$OPTARG"
  ;;
  esac
done
