select top 500 
* 
from {{ source ('source_1', 'orders') }}