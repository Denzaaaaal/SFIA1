#!/bin/bash

mkdir ./logs
pytest test/testing.py
coverage report -m < ./logs