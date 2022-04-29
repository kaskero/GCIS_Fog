export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
#sudo kubectl config set-context default
kubectl delete deploy --all

# #Pseudocodigo Escanea los nodos que están encendidos
# remote_cmd= "sudo /usr/local/bin/k3s-uninstall.sh"
#  ssh -o StrictHostKeyChecking=no ubuntu@$node_ip \'$remote_cmd\' # El ssh sería directamente a workeri
#  echo
# remote_cmd="sudo rm -rf /var/lib/rancher/k3s"
# ssh -o StrictHostKeyChecking=no ubuntu@$node_ip \'$remote_cmd\' # El ssh sería directamente a workeri

kubectl delete nodes --all

# Desinstalo k3s en el master
sudo /usr/local/bin/k3s-uninstall.sh
sudo rm -rf /var/lib/rancher/k3s
