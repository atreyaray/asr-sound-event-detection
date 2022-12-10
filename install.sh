#!/bin/bash  
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt

mkdir Dataset && mkdir Preprocessed\ Dataset
cd Dataset
# if you don't have wget, manually download the zip file from 
# https://github.com/karoldvl/ESC-50/archive/master.zip and put it in the Dataset folder
wget https://github.com/karoldvl/ESC-50/archive/master.zip
unzip master.zip
rm master.zip