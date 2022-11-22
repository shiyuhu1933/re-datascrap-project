# re-datascrap-project
This is the project that scrap PDFs from website and transform target information into csv file. I highly recommend to use anaconda virtual environment.
To make life much easier, I also recommend to use Google Colab to compile the Information_Extraction_and_Data_Visualization.ipynb.

## Requirement
Python 3.8

## Installation
for DownloadPDF.py
```python
 pip install requests
 pip install bs4
```
###
for GetTextFromPDF.py
```python
 pip install lxml
 pip install PyPDF2
 pip install io
 pip install PIL
```

### To get the eng.traineddata file within the tessdata directory: wget, more information: https://github.com/tesseract-ocr/tessdata/blob/master/eng.traineddata. for conda envirionment, to successully install tesseract:
```python
conda install -c conda-forge tesseract
```

CONTACT_INFO: shiyuhu@bu.edu
