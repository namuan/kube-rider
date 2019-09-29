# Kube-Rider

A simple desktop client for Kubernetes. 
See https://deskriders.dev/tags/kuberider/ for development updates.

### Features

[✓] Uses kubectl  
[✓] Display kubectl commands for learning  
[✓] Context and Namespace switching  
[✓] Pod list and watching  
[✓] Create/Delete Pods
[✓] List Pod containers and Events  
[✓] Open container logs  
[✓] Running commands in container  
[✓] Container Port forwarding  
[✓] Follow container logs

### Setup

Run `make` to display list of commands to install required dependencies in a virtual environment.

```
$ make
Run the following commands to install required dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Once everything is installed, 'make run' to run the application
```

Then `make run` should startup the application.

```
$ make run
```
