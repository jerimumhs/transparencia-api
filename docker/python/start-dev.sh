#!/bin/sh
export FLASK_APP=transparencia_api
export FLASK_ENV=development

flask run -h 0.0.0.0 -p 5000