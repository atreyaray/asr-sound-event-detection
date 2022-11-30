# README

### Getting Started

```bash
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt

mkdir Dataset && mkdir Preprocessed\ Dataset
```
cd Dataset
# if you don't have wget, manually download the zip file from 
# https://github.com/karoldvl/ESC-50/archive/master.zip and put it in the Dataset folder
wget https://github.com/karoldvl/ESC-50/archive/master.zip
unzip master.zip
rm master.zip
```



### Important Links 

Dataset - [here](https://github.com/karolpiczak/ESC-50)

Sample Code Implementation - [here](https://github.com/karolpiczak/paper-2015-esc-dataset/blob/master/Notebook/ESC-Dataset-for-Environmental-Sound-Classification.ipynb)


Pydub documentation - [here](https://github.com/jiaaro/pydub/blob/master/API.markdown)

Librosa Feature documentation - [here](https://librosa.org/doc/latest/feature.html#feature)


### Dev Instructions (for contributors)

Get `pipreqsnb` library to generate requirements.txt file

```bash
pip install pipreqsnb
```

When adding a new library use (from root directory)
    
```bash
pipreqsnb . --force 
``` 

