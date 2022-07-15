import csv
from django.core.management.base import BaseCommand
from auto.models import Auto
import os
from backend.settings import BASE_DIR

class Command(BaseCommand):
    def handle(self, *args, **options):
        folder = os.path.join(BASE_DIR, "data")
        cars = f"{folder}/cars.csv"
        reader = csv.DictReader(open(cars))
        for indx, row in enumerate(reader):
            indx+=1
            Auto.objects.create(
            manufacturer=row['Марка'],
            model = row['Модель'],
            color=row['Цвет'],
            plate_number=row['Рег-ый номер'],
            production_year=row['Год выпуска'],
            vin=row['Vin'],
            certificate_id=row['Номер СТС'],
            certificate_year=row['Дата СТС'],
            )
            print(f'{indx}. {row["Марка"]} {row["Модель"]} {row["Рег-ый номер"]}')
        print('\nБаза Данных успешно загружена!')
