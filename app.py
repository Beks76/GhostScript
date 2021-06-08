import camelot

class Parser:
    def __init__(self, url: str) -> None:
        self.url = url
    
    def get_kaspi_id(self):
        try:
            tables = camelot.read_pdf(self.url, pages='all')
            # print(f"Total pages: {tables.n}")
            for rows in tables:
                for ids in rows.df.loc[1:, 3]:
                    print(ids)
        except:
            print("file not found")


if __name__ == '__main__':
    parse = Parser('../test.pdf')
    parse.get_kaspi_id()
    