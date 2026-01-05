## CPU Vs GPU
### Total model: 4107

|Stage| CPU backend | GPU Backend |
|---|---|---|
|Numeric PASS| 3657 | 2629
| Setup failure | 4 | 15 |
| IREE Compilation failure | 262 | 1082 |
| Gold Inference failure | 1 | 1 |
| IREE Inference Invocation failure | 31 | 67 |
| Inference Comparison failure | 152 | 313 |


## Failure analysis

### GPU only

|#|issue type| issue no | #model impacted | list of model | assignee | status|
|---|---|---|---|---|---|---|
