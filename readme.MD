Release Branch contains the Python-flask code which will build an application 
accepting the http requests to /hello endpoint.

Dockerfile contains the required instructions to build a docker image with the above python application.

pipeline.yaml is the pipeline file which contains:

Pool: name of the agent Pool/ build agent

job: docker build using the above Dockerfile.