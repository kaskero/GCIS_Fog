from kubernetes import client, config
import time

# Parámetros de la configuración del objeto
grupo = "misrecursos.aplicacion"
version = "v1alpha2"
namespace = "default"
plural = "aplicaciones"
nombre = "aplicacion-de-prueba"


def controlador():

	config.load_kube_config("/etc/rancher/k3s/k3s.yaml")  # Cargamos la configuracion del cluster

	cliente = client.CustomObjectsApi()  # Creamos el cliente de la API

	# print("Listado de aplicaciones desplegadas en el cluster.")
	# listado_aplicaciones=cliente.list_namespaced_custom_object(grupo,version,namespace,plural,pretty="true")
	# print(listado_aplicaciones)

	while True:
		aplicacion_deseada = cliente.get_namespaced_custom_object(grupo, version, namespace, plural, nombre)

		# aplicacion=cliente.get_cluster_custom_object("misrecursos.aplicacion","v1alpha1","aplicaciones","aplicacion-de-prueba")
		print("Especificacion del componente, campo .spec:")
		print("	Nombre: " + aplicacion_deseada["metadata"]["name"])
		print("		Componentes: " + aplicacion_deseada["spec"]["componentes"])
		print("		Imagen: " + aplicacion_deseada["spec"]["image"])
		print("		Nº de replicas: " + str(aplicacion_deseada["spec"]["replicas"]))

		aplicacion_desplegada = cliente.get_namespaced_custom_object_status(grupo, version, namespace, plural, nombre)
		print(aplicacion_desplegada == aplicacion_deseada)
		print("Estado del componente en la BBDD, campo .status:")
		print("	Nombre: " + aplicacion_desplegada["metadata"]["name"])
		print("		Componentes: " + aplicacion_desplegada["spec"]["componentes"])
		print("		Imagen: " + aplicacion_desplegada["spec"]["image"])
		print("		Nº de replicas desplegadas: " + str(aplicacion_desplegada["spec"]["replicas"]))
		
		time.sleep(1)  # Espero 1 segundo
		# print(aplicacion_desplegada)


if __name__ == '__main__':
	controlador()
