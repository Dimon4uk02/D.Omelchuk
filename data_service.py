from dataclasses import dataclass

code = [1000, 2000, 3000, 4000, 5000]
name = ["Тканини", "Одяг та білизна", "Взуття", "Трикотаж", "Галантерея"]

@dataclass
class tovar:
   code:int
   name:str


data_array = [tovar(1000, "Тканини"), tovar(2000,"Одяг та білизна"), tovar(3000,"Взуття"), tovar(4000, "Трикотаж"), tovar(5000,"Галантерея")]

def printtovar(tovar):
    '''printdovidnik function prints with names and values'''
    print("Код {code}, Назва {name}" .format(code = tovar.code, name = tovar.name))

for data in data_array:
    printtovar(data)


