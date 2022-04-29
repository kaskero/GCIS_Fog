#echo "########## ADDING YOUR USER TO SUDOERS FILE ##########"
#echo "If you already have added your current user to sudoers file,"
#echo "you can skip this part and press any key to continue"
#echo
#echo "Otherwise, execute:"
#echo "  echo \"username  ALL=(ALL) NOPASSWD:ALL\" | sudo tee /etc/sudoers.d/username"
#echo "where 'username' is your current user"
#read -p "And press Ctrl+C to execute the script again"
#echo

#echo "########## GENERATING KEYS ##########"
#echo "If you already have ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub, you can skip this part"
#echo
#echo "Otherwise, execute 'ssh-keygen' to create a private/public key"
#echo
#read -p "Press any key to continue "
#echo
#pub_key=$(cat ~/.ssh/id_rsa.pub)
#echo "ssh_authorized_keys:" > multipass.yaml
#echo "  - "$pub_key >> multipass.yaml

echo "########## INSTALLING K3S MASTER ON HOST ##########"
# host_ip=$(ifconfig mpqemubr0 | grep "inet " | awk -F: '{print $1}' | awk '{print $2}')
# host_ip=192.168.1.1
curl -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE="644" sh -s - --node-ip $host_ip # El maestro tiene una ip fija 192.168.1.1
echo

echo "########## SCANNING AVAILABLE NODES ##########" # Que todos los workers encendidos se incluyan en el cluster.

# Pseudocodigo de lo que yo me imagino para conectar los workers.
# for i in #deNodosFisicos
# do
# ping al nodo i
# if nodo i encendido 
# then
#  echo "########## INSTALLING K3S AGENT ON "$node_name" ##########"
#  node_ip=192.168.1.1 + i
#  k3s_token=$(sudo cat /var/lib/rancher/k3s/server/node-token)
# remote_cmd="'curl -sfL https://get.k3s.io | K3S_URL=https://"$host_ip":6443 K3S_TOKEN="$k3s_token" sh -s - --node-label node-type=worker'" # Quizás podamos poner varios labels para facilitarle la vida a Camilo en su futuro despliegue.
#  echo $remote_cmd
#  ssh -o StrictHostKeyChecking=no ubuntu@$node_ip \'$remote_cmd\' # El ssh sería directamente a workeri
#  echo
  
#  free -m && sync && sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches' && free -m
#  echo

# fi
# 

export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
