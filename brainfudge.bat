while getopts f:e: opt
do
  case $opt in
  f)
  more "$OPTARG" | python bfr.py
  ;;
  e)
  python bfr.py "$OPTARG"
  ;;
  esac
done
