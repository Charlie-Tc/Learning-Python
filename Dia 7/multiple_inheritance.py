class Father:
    def __init__(self, name, paternal_surname):
        self.name = name
        self.paternal_surname = paternal_surname

class Mother:
    def __init__(self, name, maternal_surname):
        self.name = name
        self.maternal_surname = maternal_surname

class City:
    def __init__(self, city):
        self.city = city

class Son(Father, Mother, City):
    def __init__(self, name, paternal_surname, maternal_surname, age, city):
        Father.__init__(self, None, paternal_surname)
        Mother.__init__(self, None, maternal_surname)
        City.__init__(self,city)
        self.name = name
        self.age = age

father = Father('Juan', 'Park')
mother = Mother('Linda', 'Yani')

pepito = Son('Pepito', father.paternal_surname, mother.maternal_surname, 18, 'Croatia')
print(f'{pepito.name} {pepito.paternal_surname} tiene {pepito.age} años.')

liz = Son('Liz', pepito.paternal_surname, pepito.maternal_surname, 15, 'Seoyin')
print(f'{liz.name} {liz.paternal_surname} {liz.maternal_surname} tiene {liz.age} años y vive en {liz.city}')

