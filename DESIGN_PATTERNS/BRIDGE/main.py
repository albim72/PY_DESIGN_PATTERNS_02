from abc import ABCMeta, abstractmethod
import urllib.parse
import urllib.request

class ResourceContent:
    def __init__(self,imp):
        self._imp = imp
        
    def show_content(self,path):
        self._imp.fetch(path)
        
class ResourceContentFetcher(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self,path):
        pass
