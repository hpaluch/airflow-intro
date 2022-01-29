#!/bin/bash

set -euo pipefail

# This bash script is actually Jinja2 template

date
cat << 'EOF'
==== START
DS: "{{ ds }}"
TS: "{{ ts }}"
dag_run.id "{{ dag_run.id }}"
data_interval_start: "{{ data_interval_start }}"
data_interval_end: "{{ data_interval_end }}"
dag_run.logical_date: "{{ dag_run.logical_date }}"
==== END
EOF

exit 0

