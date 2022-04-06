# Tipos para la definicion de aplicaciones.

aplicacion = {
    'apiVersion': {},
    'kind': 'Aplicacion',
    'metadata':{
        'name': {},
    },
    'spec':{
        'componentes': [],
        'replicas': {}
    }
}

componente = {
    'name': {},
    'image': {},
    'previous': {},
    'next': {}
}

print("Hola")
