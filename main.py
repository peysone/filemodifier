"""
Napisz program oparty na klasach i dziedziczeniu, który odczyta wejściowy plik,
następnie zmodyfikuje go i wyświetli w terminalu jego zawartość, a na końcu zapisze w wybranej lokalizacji.

Uruchomienie programu przez terminal:
python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>

 <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv, in.json lub in.txt
 <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość,
 np. out.csv, out.json, out.txt lub out.pickle

 <zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0,
 natomiast "wartosc" zmianą która ma trafić na podane miejsce.

Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.json”.

Przykład działania:
python main.py in.json out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
Z pliku in.json ma wyjść plik out.csv:
gitara,3,7,0
kanapka,12,5,kubek
pedzel,17,34,5
plakat,czerwony,8,0
Wymagane formaty:

.csv
.json
.txt
.pickle
"""


import csv
import sys
import json
import pickle


def modify_data(data, changes):
    for change in changes:
        change_values = change.split(',')
        column = int(change_values[0])
        row = int(change_values[1])
        value = change_values[2]
        if row < len(data) and column < len(data[row]):
            data[row][column] = value


def read_csv(file):
    rows = []
    reader = csv.reader(file)
    for row in reader:
        rows.append(row)
    return rows


def read_json(file):
    return json.load(file)


def read_txt(file):
    lines = file.read().splitlines()
    data = []
    for line in lines:
        row = line.split(',')
        data.append(row)
    return data



def read_pickle(file):
    return pickle.load(file)


def save_csv(data, file):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(data)

def save_json(data, file):
    json.dump(data, file)


def save_txt(data, file):
    for row in data:
        file.write(','.join(row) + '\n')


def save_pickle(data, file):
    pickle.dump(data, file)


def modify_file(input_file, output_file, changes):
    extension = input_file.split('.')[-1].lower()

    with open(input_file, 'r') as file:
        if extension == 'csv':
            data = read_csv(file)
        elif extension == 'json':
            data = read_json(file)
        elif extension == 'txt':
            data = read_txt(file)
        elif extension == 'pickle':
            data = read_pickle(file)
        else:
            return

    if data is None:
        return

    modify_data(data, changes)

    with open(output_file, 'w') as file:
        if extension == 'csv':
            save_csv(data, file)
        elif extension == 'json':
            save_json(data, file)
        elif extension == 'txt':
            save_txt(data, file)
        elif extension == 'pickle':
            save_pickle(data, file)


input_file = sys.argv[1]
output_file = sys.argv[2]
changes = sys.argv[3:]

modify_file(input_file, output_file, changes)

