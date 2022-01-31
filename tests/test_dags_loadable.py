
# Verify that DAGs are at least loadable
# test integrity of all DAGs, from:
# - https://airflowsummit.org/slides/j2-Ensuring-your-DAGs-work-before-going-to-production.pdf
from os import path
import pytest
import pprint

from airflow.models import DagBag

DAG_FOLDER = path.join(path.dirname(__file__), "..")

@pytest.fixture()
def dagbag():
    return DagBag(dag_folder=DAG_FOLDER, include_examples=False)

def test_dagbag(dagbag):
    assert dagbag.import_errors == {}

def test_dags_loaded(dagbag):
    for dag_id in ['bash_template']:
        dag = dagbag.get_dag(dag_id=dag_id)
        assert dag is not None
        assert dag.dag_id == dag_id

