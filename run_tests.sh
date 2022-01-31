#!/bin/bash

set -xe
cd $(dirname $0)
PATH=~/.local/bin:$PATH
pytest -vv tests/
exit 0
