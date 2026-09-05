$serviceHostName = "flower-sample.kubeflow.example.com"
$ingressHost = "localhost"
$ingressport = 8080
$modelName = "flower-sample"

hey -z 30s -c 5 -m POST -host ${serviceHostName} -D .\inference-input.json "http://${ingressHost}:${ingressPort}/v1/models/${modelName}:predict"