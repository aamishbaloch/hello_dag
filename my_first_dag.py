from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'aamish',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 11),
    'email': ['aamish.baloch@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('Hello', default_args=default_args)


t1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Hello from Task 1"',
    dag=dag)

t2 = BashOperator(
    task_id='task_2',
    bash_command='echo "Hello from Task 2"',
    dag=dag)

t3 = BashOperator(
    task_id='task_3',
    bash_command='echo "Hello from Task 3"',
    dag=dag)

t4 = BashOperator(
    task_id='task_4',
    bash_command='echo "Hello from Task 4"',
    dag=dag)


t2.set_upstream(t1)
t3.set_upstream(t2)
t4.set_upstream(t3)
