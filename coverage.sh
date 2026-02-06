#!/bin/bash
# Run coverage for all tests
python -m coverage run manage.py test . && python -m coverage report
