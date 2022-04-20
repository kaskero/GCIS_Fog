Esta carpeta contiene ficheros de pruebas para desplegar un controlador de aplicaciones en Kubernetes.

Tres maneras de funcionar en este momento:

- Utilizar el fichero "mi_controlador_aplicaciones.py", de esta forma, se incorporará el CRD de aplicación y se iniciará el controlador. Después, con el script "solicitar_nueva_aplicacion.py", podemos añadir aplicaciones en Kubernetes.
	
- Utilizar "mi_controlador_componentes.py" y "mi_controlador_aplicaciones_v2.py". De esta forma, tendremos componentes y aplicaciones como objetos en Kubernetes. El script para añadir aplicaciones sigue siendo válido "solicitar_nueva_aplicacion.py".

- Desplegar en kubernetes los ficheros "/ficherosdocker/application_controller_deployment.yaml" y "/ficherosdocker/component_controller_deployment.yaml". Estos ficheros despliegan los controladores de componentes y aplicaciones. Para crear una aplicacion ejecutar "solicitar_nueva_aplicacion.py".

Es necesario descargar el resto de ficheros para disponer de todas las dependencias.
