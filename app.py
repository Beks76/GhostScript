import sys
import camelot
from tqdm import tqdm

import re

import numpy as np

from pdf2image import convert_from_path
import easyocr

class Parser:
    def __init__(self, url: str) -> None:
        self.url = url
    
    def get_kaspi_id(self):
        # try:
        ids_arr = []
        tables = camelot.read_pdf(self.url, pages='all')
        print(f"Total pages: {tables.n}")
        print("Parsing started...")
        for rows in tables:
            for ids in rows.df.loc[1:, 3]:
                s = ""
                digits = re.findall(r'\d', ids)
                ids_arr.append(s.join(digits))

        for i, id_ in enumerate(ids_arr):    
            if ("cid" or "[" or "]" or ")" or ")") in s.join(id_.split()):
                print("Can't define the font")
                self.ocr_for_id()
                break
        
        
        self.arr_to_txt(ids_arr)

        # except:
        #     print("file not found")

    def arr_to_txt(self, source):
        with open('result.txt', 'w') as f:
            for item in source:
                f.write("%s\n" % item)

    def ocr_for_id(self):
        reader = easyocr.Reader(['ru', 'en'])
        images = convert_from_path(self.url)
        pages = len(images)
        ids_arr = []
        for i in range(pages):
            bounds = reader.readtext(np.array(images[i]), detail=0)
            txt = str(bounds)
            ids = re.findall(r'(\d{5}\ \d{4}|\d{3}\ \d{3}\ \d{3})', txt)
            
            for id_ in ids:
                digit = re.findall(r'\d+', id_)
                s = ""
                ids_arr.append(s.join(digit))


        self.arr_to_txt(ids_arr)




if __name__ == '__main__':
    url = str(sys.argv[1:][0])
    parse = Parser(url)
    parse.get_kaspi_id()
    