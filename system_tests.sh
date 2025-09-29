#!/bin/bash
set -e
docer_path="/usr/local/bin/docker"
echo "Running system tests..."

# Test 1: addition
output=$($docer_path run --rm calc-app 1 + 2)
[ "$output" == "3" ] || { echo "FAIL: expected 3, got $output"; exit 1; }

# Test 2: subtraction
output=$($docer_path run --rm calc-app 1 - 2)
[ "$output" == "-1" ] || { echo "FAIL: expected -1, got $output"; exit 1; }

# Test 3: division
output=$($docer_path run --rm calc-app 8 / 8)
[ "$output" == "1.0" ] || { echo "FAIL: expected 1, got $output"; exit 1; }

# Test 4: multiplication
output=$($docer_path run --rm calc-app 8 '*' 8)
[ "$output" == "64" ] || { echo "FAIL: expected 64, got $output"; exit 1; }

echo "✅ All system tests passed!"
