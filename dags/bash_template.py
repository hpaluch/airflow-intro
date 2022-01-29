
# example how to use templated bash shell script

from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.utils import timezone

dag = DAG(dag_id='bash_template',
        description='Example of Jinja shell template V2',
        schedule_interval="@hourly",
        # go back 3 hours on 1st invocations
        start_date=timezone.utcnow().replace(minute=0,second=0,microsecond=0)-timedelta(hours=3)
        )

bash_jinja = BashOperator(
    bash_command="templates/bash_template.sh",
    task_id="bash_jinja",
    dag=dag,
)

bash_jinja


