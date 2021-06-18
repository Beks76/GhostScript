import sys
import camelot

import re

import numpy as np

from pdf2image import convert_from_path
import easyocr

class Parser:
    def __init__(self, url: str, to_url: str) -> None:
        self.url = url
        self.destination = to_url
    
    def get_kaspi_id(self):
        # try:
        ids_arr = []
        tables = camelot.read_pdf(self.url, pages='all')
        print(f"Total pages: {tables.n}")
        print("Parsing started...")
        for rows in tables:
            for ids in rows.df.loc[1:, 3]:
                s = ""   
                if ("cid" or "[" or "]" or ")" or ")") in s.join(ids.split()):
                    print("Can't define the font")
                    ids_arr = self.ocr_for_id()
                    break
                else:
                    digits = re.findall(r'\d', ids)
                    ids_arr.append(s.join(digits))
        
        print("End!")
        self.arr_to_txt(ids_arr, self.destination)

        # except:
        #     print("file not found")

    def arr_to_txt(self, source, destination):
        with open(destination, 'w') as f:
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

        return ids_arr




if __name__ == '__main__':
    url = str(sys.argv[1])
    to_url = str(sys.argv[2])
    parse = Parser(url, to_url)
    parse.get_kaspi_id()
    