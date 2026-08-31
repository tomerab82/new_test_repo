{{ config(tags=['20m_run']) }}

select top 900
* 
from {{ source ('source_1', 'lineitem') }}
where l_linenumber > 6