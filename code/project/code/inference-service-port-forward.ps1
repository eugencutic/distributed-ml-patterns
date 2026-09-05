


$INGRESS_GATEWAY_SERVICE= kubectl get service `
--namespace istio-system `
--selector "app=istio-ingressgateway" `
--output "jsonpath={.items[0].metadata.name}"

kubectl port-forward `
--namespace istio-system `
"service/${INGRESS_GATEWAY_SERVICE}" `
8080:80