
# example of e-mail template - JSON version of Debian DSA

import os
import sys
import json

import airflow.utils.dates
from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.operators.python import PythonOperator


# global macro passed to Jinja2 template
def load_json(json_file):
    if not os.path.isfile(json_file):
        raise Exception(f"JSON file '{json_file}' does not exist")

    with open(json_file) as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ("Unexpected parsed json object: ")
    return data

dag = DAG(
    dag_id="email_template",
    description="Test e-mail templating",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval="@daily",
    catchup=False,
    user_defined_macros={
        "load_json": load_json,
    },
) 

MOCK_DATA_ROOT = os.path.join(os.path.dirname(__file__),'mock-data')

def _prepare_html_email(templates_dict, **context):
    json_file = os.path.join(MOCK_DATA_ROOT,"dsa-data.json")
    if not os.path.isfile(json_file):
        raise Exception(f"JSON file '{json_file}' does not exist")

    context["task_instance"].xcom_push(key="email_json_file", value=json_file)

prepare_html_email = PythonOperator(
    task_id="prepare_html_email",
    python_callable=_prepare_html_email,
    dag=dag, 
    )

send_email = EmailOperator(
        task_id="send_email",
        to="ansible@localhost",
        subject="New Debian DSA alerts from AirFlow",
        html_content="templates/email_template.html",
        dag=dag, 
    )

prepare_html_email >> send_email

