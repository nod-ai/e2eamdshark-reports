# e2eamdshark-reports

This repo contains status reports of e2e runs of over 2000 models using AMD-SHARK/IREE/MLIR infra.
They are organized by date and you can find a statusreport.md, summaryreport.md, and timereport.md
for both onnx and turbine mode.

Turbine mode leverages AMD-SHARK-ModelDev's (https://github.com/nod-ai/AMD-SHARK-ModelDev) aot export to get the torch-mlir and then uses IREE compilation and runtime tools.
Onnx mode converts the pytorch/onnx models to torch-mlir using onnx-export (to .onnx) then onnx-import (converts to torch-onnx IR) + torch-mlir tools. Then, IREE compilation and runtime tools are used to run the IR.

You can find wether they pass each phase of the process (statusreport.md), times for each phase per model (timereport.md), and overall e2e stats of running all the models (summaryreport.md) in these reports.
Both modes are compared to torch references for validation, which determines if the inference phase passes.

The infra used to run all these models e2e can be found here with more details on implementation: https://github.com/nod-ai/AMD-SHARK-TestSuite/tree/main/e2eamdshark.


## Regression Tracking Graph:

[here](https://nod-ai.github.io/e2eamdshark-reports/track_test_data/regression_comparison_graph.html)
