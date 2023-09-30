class FileManager:
    def __init__(self,filename,mode,encod):
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.file = None

    # def __str__(self):
    #     return "komunikat FM..."

    def __repr__(self):
        return "tworzymy dostęp do operacji na plikach..."

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()



# fm = FileManager("xyz.txt","r","utf-8")
# print(fm)

with FileManager('test.txt',"w",'utf-8') as f:
    f.write("to jest wpis testowy managera...")
    print(type(f))

with FileManager('abc.txt',"a",'utf-8') as f:
    f.write("to jest cykliczny wpis testowy managera...")

print(f.closed)

with open('costam.dat','w',encoding='utf-8') as g:
    g.write("abc123")

print(g.closed)
