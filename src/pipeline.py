from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

seven_days_ago = datetime.combine(datetime.today() - timedelta(1),
                                  datetime.min.time())

default_args = {
    'owner': 'umayrh',
    'depends_on_past': False,
    'start_date': seven_days_ago,
    'email': ['umayrh@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('pipeline', default_args=default_args)

t0 = FileSensor(
    task_id="senseFile",
    filepath="/etc/hosts",
    fs_conn_id='fs_local',
    dag=dag)

t1 = BashOperator(
    task_id='task1',
    depends_on_past=False,
    bash_command='echo start',
    dag=dag)

t2 = BashOperator(
    task_id='task2',
    depends_on_past=False,
    bash_command='cat /etc/hosts',
    trigger_rule='all_success',
    dag=dag)

t3 = BashOperator(
    task_id='task3',
    depends_on_past=False,
    bash_command='echo last task',
    trigger_rule='all_success',
    dag=dag)

t2.set_upstream(t1)
t3.set_upstream(t2)
