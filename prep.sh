#!/bin/bash
which python3
source /zenviroment/bin/activate
#source activate
ls
which python3
uvicorn jiol:app --port 8080

