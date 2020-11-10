from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "Vicky",
    "depends_on_past": False,
    "start_date": datetime(2020, 11, 8),
    "email": ["vicky@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}  

dag = DAG("Assignment1",default_args = default_args,schedule_interval = timedelta(1))

task = BashOperator(task_id ="CreateDirectory",bash_command="mkdir test_dir" ,dag=dag)