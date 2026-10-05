{{ config(tags=['hr_run']) }}

select top 50000 
* 
from {{ source ('airline_source_1', 'flight_activity') }}