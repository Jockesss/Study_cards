#!/bin/bash

pipenv shell
pipenv run uvicorn manage:create_app --factory --host 0.0.0.0 --port 8001
