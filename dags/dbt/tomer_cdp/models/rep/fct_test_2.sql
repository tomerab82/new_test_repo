select 
* 
from {{ref('fct_test_1')}} t1
inner join {{ref('fct_test_1')}} as t2 on t1.l_orderkey = t2.l_orderkey
order by 1,2