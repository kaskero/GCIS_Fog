# Tipos para la definicion de aplicaciones.
import yaml
import json

def CRD_app():
    with open("/home/julen/Desktop/GCIS_Fog/Extender_Kubernetes/ownresources/application_definition.yaml", 'r') as stream:
        CRD_aplicacion = yaml.safe_load(stream)
    return CRD_aplicacion

def aplicacion(N):
    # N identifica el numero de componentes de la aplicacion.
    aplicacion = {
        'apiVersion': {},
        'kind': 'Aplicacion',
        'metadata':{
            'name': {},
        },
        'spec':{
            'componentes': [0]*N,
            'replicas': {}
        }
    }
    return aplicacion


def componente(nombre, imagen, anterior, siguiente):
    componente = {
        'name': nombre,
        'image': imagen,
        'previous': anterior,
        'next': siguiente
    }
    return componente

def despliegue_aplicacion(nombre):
    with open("/home/julen/Desktop/multipass_k3s/1-create-deployment.yaml", 'r') as stream:
        despliegue_de_fichero = yaml.safe_load(stream)
    despliegue_de_fichero['metadata']['name'] = despliegue_de_fichero['metadata']['name'] + '-' +nombre
    return despliegue_de_fichero
    despliegue = {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {
            'name': 'nginx-deployment',
            'labels':{
                'app': 'nginx'
            }
        },
        'spec': {
            'containers': {
                'name': 'nginx',
                'image': 'piotrzan/nginx-demo:green',
                'ports': {
                    'containerPort': '80'
                },
                'resources': {
                    'requests': {
                        'cpu': '50m',
                        'memory': '8M'
                    },
                    'limits': {
                        'cpu': '100m',
                        'memory': '16M'
                    }
                }
            }
        },
        'nodeSelector': {
            'node-type': 'multipass'
        }
    }
    # return despliegue