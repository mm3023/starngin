#!/bin/bash
which python3
cd /zenviroment/bin
source activate
cd /zenviroment
ls
which python3
uvicorn jiol:app --port 8080

