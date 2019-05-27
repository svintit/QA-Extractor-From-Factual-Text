SHELL=bash

SERVICE_NAME=q_extractor
PORT=9331

VERSION := latest


build:
	    echo ${VERSION} > version
	    docker build --network host -t registry:5000/jenkins/${SERVICE_NAME}:${VERSION} . --no-cache

push:
	    echo ${VERSION} > version
	    docker push registry:5000/jenkins/${SERVICE_NAME}:${VERSION}

