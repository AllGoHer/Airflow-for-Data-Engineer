from datetime import datetime
from airflow.decorators import dag, task

@dag(
    schedule = '@daily',
    start_date = datetime(2026, 5, 18),
    catchup=False,
    tags=["demo", "taskflow"]
)
def taskflow_demo():
    @task
    def extract():
        data = ["apple", "banana", "cherry"]
        return data
    
    @task
    def transform(data):
        transformed_data = [item.upper() for item in data]
        return transformed_data
    
    @task
    def load(data):
        for item in data:
            print(f"Loaded: {item}")

    load(transform(extract()))

taskflow_demo()

