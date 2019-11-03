from abc import ABCMeta, abstractmethod

class BaseClass(metaclass = ABCMeta):
    __metaclass__ = ABCMeta
    @abstractmethod
    def printerMetot(self): 
        return("Base Dosya")

class Personel(BaseClass):
    def printerMetot(self):
        return "Personel Dosyası Yazdırlıdı"

class Ogrenci(BaseClass):
    def printerMetot(self):
        return "Öğrenci Dosyası Yazdırlıdı"



per  = Personel()
print(per.printerMetot())

ogr = Ogrenci()
print(ogr.printerMetot())