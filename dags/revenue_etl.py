from datetime import datetime
import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Import your custom transformation logic
from transformer import calculate_revenue_for_order

# Define the DAG and default arguments
dag = DAG(
    'revenue_etl',
    schedule_interval='@daily',
    start_date=datetime(2023, 8, 6),
)

# Task to execute the custom transformation logic
task_transform_data = PythonOperator(
    task_id='transform_data',
    python_callable=calculate_revenue_for_order,
    op_kwargs={'input_data': os.path.join(f"{os.getenv('AIRFLOW_HOME')}",'input_data/data.xlsx'), 
               'input_rate': os.path.join(f"{os.getenv('AIRFLOW_HOME')}",'input_data/rates.xlsx')},  # Path to the input Excel file
    dag=dag,
)

# Set the task dependencies
task_transform_data