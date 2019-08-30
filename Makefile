export PROJECTNAME=$(shell basename "$(PWD)")

.SILENT: ; # no need for @

setup: ## Setup virtual environment and install dependencies
	echo "Run the following commands to install required dependencies"
	echo "python3 -m venv venv"
	echo "source venv/bin/activate"
	echo "pip install -r requirements.txt"
	echo "Once everything is installed, 'make run' to run the application"

venv: ## Activates local venv
	source venv/bin/activate

uic: res ## Converts ui files to python
	for i in `ls resources/ui/*.ui`; do FNAME=`basename $${i} ".ui"`; ./venv/bin/pyuic5 $${i} > "kuberider/generated/$${FNAME}.py"; done

res: venv ## Generates and compresses resource file
	./venv/bin/pyrcc5 -compress 9 -o kuberider/resources_rc.py kuberider/resources.qrc

icns: ## Generates icon files from svg
	echo "Run ./mk-icns.sh kuberider/images/kuberider.svg kuberider"

run:  ## Runs the application
	export PYTHONPATH=`pwd`:$${PYTHONPATH} && \
	python3 kuberider/main.py

.PHONY: help
.DEFAULT_GOAL := setup

help: Makefile
	echo
	echo "  Choose a command run in "$(PROJECTNAME)":"
	echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo