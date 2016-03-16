import pandas
class link():
    def __init__(self,address,dest,number):
        self.address=address
        self.dest=dest
        self.file=pandas.read_html(address)
        self.number=number
    def toexcel(self):
        self.file[int(self.number)-int(1)].to_excel(self.dest)
    def tocsv(self):
        self.file[int(self.number)-int(1)].to_csv(self.dest)
    def tojson(self):  
        self.file[int(self.number)-int(1)].to_json(self.dest)
    def toxml(self):
        self.file[int(self.number)-int(1)].to_xml(self.dest)



