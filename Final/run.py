import re
import os.path
from datetime import datetime
from pipeline import pipeline


# Function to clean text and then put it on the txt file for further training
def text_cleaner(text):
    letters_only = re.sub("[^a-zA-Z]", " ", text)
    words = letters_only.lower().split()
    line = " ".join(words)
    save_path = 'output\\'
    filename = 'test-%s.txt' % datetime.now().strftime('%Y-%m-%d-%H%M%S')
    complete_name = os.path.join(save_path, filename)
    with open(complete_name, mode='a', encoding='UTF-8', buffering=1) as a:
        a.write(line)
    print('File Generated')


# Main Function
if __name__ == "__main__":
    path = ('documents')
    path = path+"\\"
    print('Loading the files to the pipeline..')
    text = pipeline(path)
    print("Now Converting preparing the final text file")
    text_cleaner(text)
    print('All Activity Completed')
