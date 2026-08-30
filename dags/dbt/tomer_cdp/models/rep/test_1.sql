select top 1000 
* 
from {{ source ('source_1', 'lineitem') }}
where l_linenumber > 6