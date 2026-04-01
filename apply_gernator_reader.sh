sudo kubectl delete -f /home/gio81/faas-kafka-knative/Reader/Deployment.yaml
sudo kubectl delete -f /home/gio81/faas-kafka-knative/Generator/Deployment.yaml

cd /home/gio81/faas-kafka-knative/Generator
sudo docker build -t gio8134/generator:latest .
sudo docker push gio8134/generator:latest

cd /home/gio81/faas-kafka-knative/Reader
sudo docker build -t gio8134/reader:latest .
sudo docker push gio8134/reader:latest

cd /home/gio81/faas-kafka-knative/
sudo kubectl apply -f /home/gio81/faas-kafka-knative/Reader/Deployment.yaml
sudo kubectl apply -f /home/gio81/faas-kafka-knative/Generator/Deployment.yaml
