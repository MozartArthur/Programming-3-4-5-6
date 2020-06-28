import csv
from contextlib import contextmanager

@contextmanager
def opencsv(path):
   yield csv.reader(open(path))

with opencsv("MOCK_DATA.csv") as reader:
