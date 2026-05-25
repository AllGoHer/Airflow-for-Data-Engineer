#Importaciones escenciales
from datetime import datetime
from airflow.decorators import dag
from airflow.operators.bash import BashOperator

#Definir DAG
@dag(
    dag_id = "bash_operator_demo",
    start_date=datetime(2026, 5, 20),
    schedule="@daily",
    catchup=False,
    tags=['bashdemo'],
)
def bash_operator_demo():
    #definir tarea con operador bash
    List_dag_files = BashOperator(
        task_id="list_dag_folder_files",
        bash_command="echo 'Files in DAGs Folder:' && ls -lh /opt/airflow/dags",
    )

bash_operator_demo()