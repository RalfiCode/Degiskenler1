from abc import ABCMeta, abstractmethod

class BasePhone(metaclass=ABCMeta):
    def __init__(self,marka,model,fiyat):
        self.Marka = marka
        self.Model = model
        self.Fiyat = fiyat
    
    @abstractmethod
    def Sound(self):
        pass

    def __str__(self):
        return "Marka : {}\n Model : {}\n Fiyat : {}".format(self.Marka,self.Model,self.Fiyat)


class Samsung(BasePhone):
    def __init__(self,marka,model,fiyat,tedarikci):
        super(Samsung, self).__init__(marka,model,fiyat)
        self.Tedarikci = tedarikci
        
        def Sound(self):
            return "Samsung Telefon Sesi"

class Apple(BasePhone):
    def __init__(self,marka,model,fiyat,garanti):
        super(Apple, self).__init__(marka,model,fiyat)
        self.Garanti = garanti
        
        def __str__(self):
            return "{}\nGaranti Süresi : {}\nTelefon Sesi{}".format(super().__str__(),self.Garanti)
        
        def Sound(self):
            return "Apple Telefon Sesi"

class Nokia(BasePhone):
      def __init__(self,marka,model,fiyat,isletim_sistemi):
        super(Nokia, self).__init__(marka,model,fiyat)
        self.Isletim_sistemi = isletim_sistemi
        
        def Sound(self):
            return "Nokia Telefon Sesi"

apple = Apple(2)
print(Apple)