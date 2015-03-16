#!/bin/bash

# THIS TEST RUNS PY.TEST ON EXCLUSIVE_CACHE_FILE_TEST.PY A GIVEN NUMBER OF TIMES

# check if number of runs supplied
if [ $# -eq 0 ]; then
    echo "Please supply desired number of test runs as parameter"
    exit 1
fi;

# needed for py.test to find modules
export PYTHONPATH=./../..


# run tests, count errors and append error messages to file
num_errors=0
echo "THIS FILE CAN BE FREELY REMOVED WITHOUT ANY CONSEQUENCES" > "Errors.txt"

for ((i=1;i<=$1;i++)); do
  echo "Test run no. $i..."
  test_output=`py.test exclusive_cache_file_test.py`
  
  if [ $? -ne 0 ]; then
    echo "Test error!"
    let num_errors++
    echo $test_output >> "Errors.txt"
  fi;
done;

# print test summary
echo "Tests finished. $num_errors errors"
