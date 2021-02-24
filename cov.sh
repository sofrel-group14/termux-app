#!/bin/bash

./gradlew test -i --rerun-tasks | grep -e "TEST_COVERAGE_GETCODE" > coverage.txt && python3 cov.py
