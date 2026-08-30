import os
from datetime import datetime

from cosmos.constants import ExecutionMode
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "ta_dbt_db", "schema": "schema_1"},

    ))

dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig("/usr/local/airflow/dags/dbt/tomer_cdp",),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        execution_mode=ExecutionMode.LOCAL,
        # 👇 CHANGED THIS PATH to point to your Dockerfile's environment
        dbt_executable_path="/usr/local/airflow/dbt_venv/bin/dbt" 
    ),
    schedule="*/5 * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="dbt_dag",
)