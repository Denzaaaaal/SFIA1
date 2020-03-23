#!/bin/bash

mkdir -p ./log 
echo "Testing HTTP Codes..."
pytest test/testing.py < log/testing_$(date +"%d-%m-%Y").txt | egrep 'passed|failed|short test summary info|FAILED'

echo "Generating coverage report..."
coverage report -m | grep "TOTAL"