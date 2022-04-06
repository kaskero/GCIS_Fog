from kubernetes import client, config
import mi_watcher_aplicaciones
import tipos

# Parámetros de la configuración del objeto
grupo = "misrecursos.aplicacion"
version = "v1alpha3"
namespace = "default"
plural = "aplicaciones"
# nombre = "aplicacion-de-prueba"
componente = tipos.componente


def controlador():

	config.load_kube_config("/etc/rancher/k3s/k3s.yaml")  # Cargamos la configuracion del cluster

	cliente = client.CustomObjectsApi()  # Creamos el cliente de la API

	# print("Listado de aplicaciones desplegadas en el cluster.")
	# listado_aplicaciones=cliente.list_namespaced_custom_object(grupo,version,namespace,plural,pretty="true")
	# print(listado_aplicaciones)

	mi_watcher_aplicaciones.mi_watcher(cliente)


def mostrar_datos(nombre, cliente):

	if version == 'v1alpha2':
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

	if version == 'v1alpha3':
		aplicacion_deseada = cliente.get_namespaced_custom_object(grupo, version, namespace, plural, nombre)
		# aplicacion=cliente.get_cluster_custom_object("misrecursos.aplicacion","v1alpha1","aplicaciones","aplicacion-de-prueba")
		print("Especificacion de aplicacion, campo .spec:")
		print("Nombre: " + aplicacion_deseada["metadata"]["name"])
		print("Componentes: ")
		for i in aplicacion_deseada['spec']['componentes']:
			print("  Nombre del componente: " + i['name'])
			print("  	- Imagen: " + i['image'])
			print("  	- Componente anterior: " + i['previous'])
			print("  	- Siguiente componente: " + i['next'])
		print("		Nº de replicas: " + str(aplicacion_deseada["spec"]["replicas"]))

		aplicacion_desplegada = cliente.get_namespaced_custom_object_status(grupo, version, namespace, plural, nombre)
		print(aplicacion_desplegada == aplicacion_deseada)
		print("Estado de la aplicacion en la BBDD, campo .status:")
		print("Nombre: " + aplicacion_desplegada["metadata"]["name"])
		print("Componentes: ")
		for i in aplicacion_deseada['spec']['componentes']:
			print("  Nombre del componente: " + i['name'])
			print("  	- Imagen: " + i['image'])
			print("  	- Componente anterior: " + i['previous'])
			print("  	- Siguiente componente: " + i['next'])
		print("		Nº de replicas desplegadas: " + str(aplicacion_desplegada["spec"]["replicas"]))

	# time.sleep(1)  # Espero 1 segundo
	# print(aplicacion_desplegada)


def conciliar_spec_status(nombre, cliente):

	# Esta funcien es llamada por el watcher cuando hay un evento ADDED o MODIFIED.
	# Habria que chequear las replicas, las versiones...
	# De momento esta version solo va a mirar el numero de replicas.
	# Chequea si la aplicacion que ha generado el evento esta al día en .spec y .status

	# Miro el spec.
	aplicacion_deseada = cliente.get_namespaced_custom_object(grupo, version, namespace, plural, nombre)

	# Miro el status.
	aplicacion_desplegada = cliente.get_namespaced_custom_object_status(grupo, version, namespace, plural, nombre)

	# Compruebo.

	if aplicacion_deseada['spec']['replicas'] != aplicacion_desplegada['status']['replicas']:
		if aplicacion_deseada['spec']['replicas'] > aplicacion_desplegada['status']['replicas']:
			pass
			# En caso de modificacion del numero de replicas o objeto recien añadido.
			# Habria que desplegar las replicas restantes.
			# for i in aplicacion_deseada['spec']['replicas'] - aplicacion_desplegada['status']['replicas']:
			# 	desplegar_replica()
		if aplicacion_deseada['spec']['replicas'] < aplicacion_desplegada['status']['replicas']:
			pass
			# En caso de modificacion del numero de replicas.
			# Habria que eliminar las replicas sobrantes.
			# for i in aplicacion_deseada['status']['replicas'] - aplicacion_desplegada['spec']['replicas']:
			# 	desplegar_replica()


if __name__ == '__main__':
	controlador()
