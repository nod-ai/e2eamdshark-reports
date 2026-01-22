# Top issues

https://github.com/iree-org/iree/issues/22942 : Kunwar : 378 models

https://github.com/iree-org/iree/issues/22957 : Max : 69 models

https://github.com/iree-org/iree/issues/23013 : Nirvedh : 41 models

https://github.com/iree-org/iree/issues/22977 : Zach : 10 models





# ONNX model Passing status 

### ONNX model Zoo

**TOTAL TESTS = 4107**

|Stage|CPU|GPU|                                                                   
|--|--|--|
| Setup | 4103 | 4092 | 
| IREE Compilation | 3984 | 3486|
| Gold Inference | 3983 | 3486|
| IREE Inference Invocation | 3970 | 3371|
| Inference Comparison (PASS) | 3690 | 3222|

### HF top-1k model

**TOTAL TESTS = 507**

|Stage|CPU|GPU|
|--|--|--|
| Setup | 495 | 496 | 
| IREE Compilation | 405 | 400|
| Gold Inference | 403 | 398|
| IREE Inference Invocation | 399 | 396|
| Inference Comparison (PASS) | 383 | 378|

### Other ONNX models

**TOTAL TESTS = 2361**

|Stage|CPU|GPU|
|--|--|--|
| Setup | 1987 | 975 | 
| IREE Compilation | 1964 | 859|
| Gold Inference | 1964 | 859|
| IREE Inference Invocation | 1963 | 858|
| Inference Comparison (PASS) | 1840 | 810|

