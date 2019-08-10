export PROJECTNAME=$(shell basename "$(PWD)")

.SILENT: ;               # no need for @

venv: ## Activates local venv
	source venv/bin/activate

uic: res ## Converts ui files to python
	for i in `ls resources/ui/*.ui`; do FNAME=`basename $${i} ".ui"`; ./venv/bin/pyuic5 $${i} > "kuberider/generated/$${FNAME}.py"; done

res: venv ## Generates and compresses resource file
	./venv/bin/pyrcc5 -compress 9 -o kuberider/resources_rc.py kuberider/resources.qrc

icns: ## Generates icon files from svg
	echo "Run ./mk-icns.sh kuberider/images/kuberider.svg kuberider"

.PHONY: help
.DEFAULT_GOAL := help

help: Makefile
	echo
	echo " Choose a command run in "$(PROJECTNAME)":"
	echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo