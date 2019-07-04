#!/bin/bash
BASE_URL = http://localhost:8000
curl --data "token=$1&amount=$2&text=$3"  BASE_URL/submit/income/
