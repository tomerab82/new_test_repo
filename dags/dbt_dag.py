import os
from datetime import datetime

from cosmos.constants import ExecutionMode
from cosmos import DbtDag, ProjectConfig, ProfileConfig, RenderConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "ta_dbt_db", "schema": "schema_1"},

    ))

dbt_snowflake_dag_hr_run = DbtDag(
    project_config=ProjectConfig("/usr/local/airflow/dags/dbt/tomer_cdp",),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    render_config=RenderConfig(select=["tag:hr_run"]),
    execution_config=ExecutionConfig(execution_mode=ExecutionMode.LOCAL,dbt_executable_path="/usr/local/airflow/dbt_venv/bin/dbt"),
    schedule="0 * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="dbt_dag_hr_run",
)

dbt_snowflake_dag_20m_run = DbtDag(
    project_config=ProjectConfig("/usr/local/airflow/dags/dbt/tomer_cdp",),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    render_config=RenderConfig(select=["tag:20m_run"]),
    execution_config=ExecutionConfig(execution_mode=ExecutionMode.LOCAL,dbt_executable_path="/usr/local/airflow/dbt_venv/bin/dbt"),
    schedule="*/20 * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="dbt_dag_20m_run",
)