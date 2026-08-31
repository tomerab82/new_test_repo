{{ config(tags=['hr_run']) }}

select * from {{ source('source_2', 'ref_lines') }}