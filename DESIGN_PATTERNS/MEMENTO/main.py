class Memento:
    def __init__(self,file,content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self,file):
        self.file = file
        self.content = ""
        
    
