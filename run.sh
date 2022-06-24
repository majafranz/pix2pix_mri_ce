#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Usage: ./run.sh [jupyter|bash]"
	exit 1
fi

if [ "$1" = "bash" ]; then
    /bin/bash
elif [ "$1" = "jupyter" ]; then
    jupyter notebook --port=8888 --no-browser --ip=0.0.0.0 --NotebookApp.token='' --NotebookApp.password=''
else
    echo "Usage: ./run.sh [jupyter|bash]"
fi
