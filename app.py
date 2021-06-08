import sys
import camelot
from tqdm import tqdm

class Parser:
    def __init__(self, url: str) -> None:
        self.url = url
    
    def get_kaspi_id(self):
        try:
            ids_arr = []
            tables = camelot.read_pdf(self.url, pages='all')
            print(f"Total pages: {tables.n}")
            print("Parsing started...")
            for rows in tqdm(tables):
                for ids in rows.df.loc[1:, 3]:
                    ids_arr.append(ids)
            
            for i, id_ in enumerate(ids_arr):    
                s = ""
                ids_arr[i] = s.join(id_.split())
            
            self.arr_to_txt(ids_arr)

        except:
            print("file not found")

    def arr_to_txt(self, source):
        with open('result.txt', 'w') as f:
            for item in source:
                f.write("%s\n" % item)

if __name__ == '__main__':
    url = str(sys.argv[1:][0])
    parse = Parser(url)
    parse.get_kaspi_id()
    