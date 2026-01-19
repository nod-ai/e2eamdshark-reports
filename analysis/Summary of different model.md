# Top issues

https://github.com/iree-org/iree/issues/23171 : Ben : 400+ models

https://github.com/iree-org/iree/issues/22942 : Kunwar : 378 models

https://github.com/iree-org/iree/issues/23185 : Eric Feng : 119 models

https://github.com/iree-org/iree/issues/22957 : Max : 69 models

https://github.com/iree-org/iree/issues/23013 : Unassigned : 41 models

https://github.com/iree-org/iree/issues/22977 : Zach : 10 models





# ONNX model Passing status 

### ONNX model Zoo

**TOTAL TESTS = 4107**

|Stage|CPU|GPU|                                                                   
|--|--|--|
| Setup | 4103 | 4092 | 
| IREE Compilation | 3984 | 3375|
| Gold Inference | 3983 | 3375|
| IREE Inference Invocation | 3958 | 3260|
| Inference Comparison (PASS) | 3282 | 2864|

### HF top-1k model

**TOTAL TESTS = 507**

|Stage|CPU|GPU|
|--|--|--|
| Setup | 496 | 497 | 
| IREE Compilation | 406 | 401|
| Gold Inference | 404 | 399|
| IREE Inference Invocation | 401 | 397|
| Inference Comparison (PASS) | 380 | 375|

### Other ONNX models

**TOTAL TESTS = 2361**

|Stage|CPU|GPU|
|--|--|--|
| Setup | 1987 | 975 | 
| IREE Compilation | 1964 | 859|
| Gold Inference | 1964 | 859|
| IREE Inference Invocation | 1963 | 858|
| Inference Comparison (PASS) | 1840 | 810|

