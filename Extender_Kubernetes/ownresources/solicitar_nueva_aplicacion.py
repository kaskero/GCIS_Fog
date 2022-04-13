from kubernetes import client, config
import tipos

grupo = "misrecursos.aplicacion"
version = "v1alpha3"
namespace = "default"
plural = "aplicaciones"

def desplegar(aplicacion):
    config.load_kube_config("/etc/rancher/k3s/k3s.yaml")
    cliente = client.CustomObjectsApi()
    # Creo un objeto aplicacion en la BBDD de kubernetes.
    # El watcher detectará un evento ADDED y le mandará al controlador conciliar los estados spec y status.
    cliente.create_namespaced_custom_object(grupo, version, namespace, plural, aplicacion)

def solicitar_nueva_aplicacion():
    nombre_app = None
    N_de_componentes = '0'
    N_de_replicas = '0'
    while nombre_app == None:
        print("¿Como quieres que se llame la aplicacion? (El nombre en kubernetes sera aplicacion-solicitada-TUNOMBRE)")
        nombre_app = input()
        if not (str.isalnum(nombre_app) and str.islower(nombre_app)):
            nombre_app = None
            print('El nombre debe estar compuesto de caracteres alfanumericos y minúsculas.')
    while N_de_componentes == '0':
        print("¿Cuantos componentes quieres en la aplicacion?")
        N_de_componentes=input()
        if int(N_de_componentes) > 23 or int(N_de_componentes) <= 1:
            N_de_componentes = '0'
            print('El numero de componentes debe ser menor de 23 y mayor que 1.')
    while N_de_replicas == '0':
        print("¿Cuantas replicas quieres?")
        N_de_replicas=input()
        if int(N_de_replicas) > 10 or int(N_de_replicas) <= 0:
            N_de_replicas = '0'
            print('El numero de replicas debe estar entre 0 y 10.')
    aplicacion = tipos.aplicacion(int(N_de_componentes))
    aplicacion['apiVersion'] = grupo + '/' + version
    aplicacion['metadata']['name'] = "aplicacion-solicitada-" + nombre_app
    aplicacion['spec']['replicas'] = int(N_de_replicas)
    for i in range(int(N_de_componentes)):
        #i=int(i)
        if i == 0:
            aplicacion['spec']['componentes'][i] = tipos.componente('d', "imagen-componente-d", "none", "e") #OJO, si asigno None, luego no está en el diccionario. Mejor asigno none como string.
        elif i == int(N_de_componentes)-1:
            aplicacion['spec']['componentes'][i] = tipos.componente(chr(100+i), "imagen-componente-" + chr(100+i), chr(100+i-1), "none")
        else:
            aplicacion['spec']['componentes'][i] = tipos.componente(chr(100+i), "imagen-componente-" + chr(100+i), chr(100+i-1), chr(100+i+1))

    desplegar(aplicacion)


if __name__ == "__main__":
    solicitar_nueva_aplicacion()