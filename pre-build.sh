#!/bin/bash

for i in `ls resources/ui/*.ui`; do FNAME=`basename $i ".ui"`; ./venv/bin/pyuic5 $i > "kuberider/generated/$FNAME.py"; done

./venv/bin/pyrcc5 -compress 9 -o kuberider/resources_rc.py kuberider/resources.qrc