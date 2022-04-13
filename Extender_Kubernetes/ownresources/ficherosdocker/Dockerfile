FROM python:3.8-slim-buster
COPY ./application_definition.yaml /application_definition.yaml
COPY ./mi_watcher_aplicaciones_v2.py /mi_watcher_aplicaciones_v2.py
COPY ./mi_controlador_aplicaciones_v2.py /mi_controlador_aplicaciones_v2.py
COPY ./tipos.py /tipos.py
CMD mi_controlador_aplicaciones_v2.py
