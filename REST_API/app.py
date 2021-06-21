from ilovepdf import ILovePdf
PUBLIC_KEY = 'project_public_01f6bcca073f4a2f5a160f4bc4add753_VfRD54aeb550af0b64c92107e42d296e7cd6c'
SECRET_KEY = 'secret_key_92e195c4d2a4dc68472373540887e7ae_85qfUcf8c4c8568aba2a705bc96e3de8f4bfb'
if __name__ == "__main__":
    pdf = ILovePdf(PUBLIC_KEY, SECRET_KEY)
    pdf.new_task("extract")
    pdf.add_file("test3.pdf")
    pdf.execute()
    code = pdf.download("res")

