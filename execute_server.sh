#!/bin/bash


echo executing server... 

python -m uvicorn main:app --reload

pause