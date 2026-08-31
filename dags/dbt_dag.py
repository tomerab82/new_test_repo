from datetime import datetime

from airflow import DAG

from cosmos import DbtTaskGroup
from cosmos.config import (
    ExecutionConfig,
    ProfileConfig,
    ProjectConfig,
    RenderConfig,
)
from cosmos.constants import ExecutionMode
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


# ------------------------------------------------------------------
# dbt profile
# ------------------------------------------------------------------

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={
            "database": "ta_dbt_db",
            "schema": "schema_1",
        },
    ),
)


# ------------------------------------------------------------------
# Shared dbt configuration
# ------------------------------------------------------------------

project_config = ProjectConfig(
    "/usr/local/airflow/dags/dbt/tomer_cdp"
)

execution_config = ExecutionConfig(
    execution_mode=ExecutionMode.LOCAL,
    dbt_executable_path="/usr/local/airflow/dbt_venv/bin/dbt",
)


# ------------------------------------------------------------------
# HR - hourly
# ------------------------------------------------------------------

with DAG(
    dag_id="dbt_dag_hr_run",
    schedule="0 * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    dbt_hr_run = DbtTaskGroup(
        group_id="dbt_hr_run",
        project_config=project_config,
        profile_config=profile_config,
        execution_config=execution_config,
        render_config=RenderConfig(
            select=["tag:hr_run"],
        ),
    )


# ------------------------------------------------------------------
# 20 minute run
# ------------------------------------------------------------------

with DAG(
    dag_id="dbt_dag_20m_run",
    schedule="*/20 * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    dbt_20m_run = DbtTaskGroup(
        group_id="dbt_20m_run",
        project_config=project_config,
        profile_config=profile_config,
        execution_config=execution_config,
        render_config=RenderConfig(
            select=["tag:20m_run"],
        ),
    )