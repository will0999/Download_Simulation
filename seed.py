import csv

from model import Computer, Resource

def loadComputers():
    computadores = []
    with open('csv/computadores.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=';')
      next(csv_reader, None)  # pula os cabeçalhos
      for row in csv_reader:
        computador = Computer(row[0], row[1], row[2])
        computadores.append(computador)
    return computadores

def loadResources():
    recursos = []
    with open('csv/recursos_digitais.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=';')
      next(csv_reader, None)  # pula os cabeçalhos
      for row in csv_reader:
        recurso = Resource(row[0], row[1], row[2], row[3])
        recursos.append(recurso)
    return recursos
