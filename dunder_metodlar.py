# 2025.03.30
# Mavzu: Dunder metodlar
# Muallif: Muhammadsodiq

class Avto:
    __num_avto = 0

    def __init__(self, make, model, rang, yil, narh):
        self.make = make
        self. model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
    
    def __str__(self):
        return f"Avto: {self.make} {self.model}"
    
    def __repr__(self):
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self, y):
        return self.narh == y.narh
    
    def __lt__(self, y):
        return self.narh < y.narh
    
    def __le__(self, y):
        return self.narh <= y.narh

    '''def __len__(self):
        return len(self)'''

class AvtoSalon:
    def __init__(self, name):
        self.name = name
        self.avtolar = []
    
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self, index, qiymat):
        self.avtolar[index] = qiymat

    def __call__(self, *qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
            else:
                return [avto for avto in self.avtolar]
    
    def __add__(self, y):
        if isinstance(y, AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {y}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon
        elif isinstance(y, Avto):
            self.add_avto(y)

    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")

salon1 = AvtoSalon('MaxAvto')
salon2 = AvtoSalon("Avto Lider")
print(repr(salon1))

# print(dir(Avto))
avto1 = Avto("Porsche", "Supra", 'kok', 2022, 18000)
avto2 = Avto("GM", "lacetti", 'qizil', 2020, 14000)
avto3 = Avto("Bugatti", "Cheeron", 'qora', 2024, 142000)
avto4 = Avto( "Mazda", "6",'Cizil', 2015, 35000)
avto5 = Avto("VoLkswagen", "PoLo", 'gora', 2015, 30000)
avto6 = Avto("Honda", "Accord", "Oq", 2017,42000)
salon1.add_avto(avto1, avto2, avto3)
print(salon1[:])

salon2(avto4,avto5,avto6)
print(salon2[:])

salon3 = salon1 + salon2
print(salon3[:])

print(avto1)
print(str(avto1))
print(repr(avto1))
print(avto1.model)

print(isinstance(4,int))

print(len(salon1))
print(salon1())