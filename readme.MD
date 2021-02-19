Release Branch contains the Python-flask code which will build an application 
accepting the http requests to /hello endpoint.


test-*.py: 
    contains basic unit tests that will check for the proper Http 200 response from the web application.

Dockerfile contains the required instructions to build a docker image with the above python application.

Requirment.txt:
    It consists of the prerequisite softwares to be installed for running the application.


Azure DevOps:

    Pipeline.yaml consists pipeline script used for setting up a basic azure devops pipelines with the job: Docker Build.
    If there is a requiremnt to push the docker image to any docker requistry, we can add a task: docker push <tagname>
    
    Pool: name of the agent Pool/ build agent

    job: docker build using the above Dockerfile..


For every new commit to the release branch, the TravisCI run wil be triggered.

TravisCI:

.travis.yml: pipeline file for making up the configurations to build the code in travis.yml.

      language: the base programming language of your code
      
      python: 
          verisons: with what versions you want to test your python code.
          
      install: 
        command to execute for installing the prerequiste softwares. here eg: requirement.txt
        
      script:
         Command/file to build your Pipeline.. 
