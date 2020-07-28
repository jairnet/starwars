#!/bin/bash

for file in planets people transport starships vehicles species films
do
    python ./manage.py loaddata $file
done