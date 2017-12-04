#!/bin/bash

cd pywren
zip -r deploy.zip jobrunner.py version.py wren.py wrenconfig.py wrenhandler.py wrenutil.py redis redis-2.10.6.dist-info

mv deploy.zip ../
