{{ config(tags=['hr_run']) }}

select top 50000 
* 
from {{ source ('source_airline', 'flight_activity') }}