# Word Corpus Creator

This tool can be used to create a word corpus from locally available documents.Word Corpus are required to build word embeddings for certain Natural Language Processing tasks.
This tool will convert the documents present in the `documents` folder into a single clean txt file that can be then passed to a word vector generator such as [GloVe](https://github.com/stanfordnlp/GloVe) created by Stanford.

## Description of the files/folders:
* `Final`: Contains all the necessary files for the tool kit
* `documents`: Put all the documents that you want to convert into this folder. Currently it can accept: `pdf`,`docx` 
* `docx2text.py`: Converts the passed docx file to text
* `pdf2text.py`: Converts the passed pdf to text
* `pipeline.py`: Picks the file from the documents folder and passes it to the correct converter
* `run.py`: This file is supposed to be executed to get the necessary text file output. This will clean the text generated from all the files and save the created text file in the correct location
* `output`: This folder will have the text file as the output. 

### NOTE: 
Final output will be a single text file that will be a combination of all the files in the document folder.  
Some sample documents are already saved in the `documents` folder for you to quickly test. 

## Requirement:
* Python: 2.7 and above
* For pdf conversion
    - *pdfminer*(python 2.7)
    - *pdfminer.six*(python 3)
* For docx conversion
    - python-docx
