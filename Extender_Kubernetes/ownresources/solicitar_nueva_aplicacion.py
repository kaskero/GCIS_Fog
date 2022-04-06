from kubernetes import client, config
import tipos

grupo = "misrecursos.aplicacion"
version = "v1alpha3"
namespace = "default"
plural = "aplicaciones"

def desplegar(aplicacion):
    config.load_kube_config("/etc/rancher/k3s/k3s.yaml")
    cliente = client.CustomObjectsApi()
    cliente.create_namespaced_custom_object(grupo, version, namespace, plural, aplicacion)

def solicitar_nueva_aplicacion():
    print("Como quieres que se llame la aplicacion? (El nombre en kubernetes sera aplicacion-solicitada-TUNOMBRE)")
    nombre_app=input()
    print("Cuantos componentes quieres en la aplicacion?")
    N_de_componentes=input()
    aplicacion = tipos.aplicacion(int(N_de_componentes))
    aplicacion['apiVersion'] = grupo + '/' + version
    aplicacion['metadata']['name'] = "aplicacion-solicitada-" + nombre_app
    aplicacion['spec']['replicas'] = 2
    for i in range(int(N_de_componentes)):
        #i=int(i)
        if i == 0:
            aplicacion['spec']['componentes'][i] = tipos.componente('D', "imagen-componente-D", "none", "E") #OJO, si asigno None, luego no está en el diccionario. Mejor asigno none como string.
        elif i == int(N_de_componentes)-1:
            aplicacion['spec']['componentes'][i] = tipos.componente(chr(68+i), "imagen-componente-" + chr(68+i), chr(68+i-1), "none")
        else:
            aplicacion['spec']['componentes'][i] = tipos.componente(chr(68+i), "imagen-componente-" + chr(68+i), chr(68+i-1), chr(68+i+1))

    desplegar(aplicacion)


if __name__ == "__main__":
    solicitar_nueva_aplicacion()