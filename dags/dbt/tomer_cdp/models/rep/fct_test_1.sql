{{ config(tags=['20m_run']) }}
select 
* 
from {{ref('test_1')}}
order by 1,2