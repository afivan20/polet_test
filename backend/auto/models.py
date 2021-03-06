
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from django.db.models.constraints import UniqueConstraint



def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)




class Auto(models.Model):
    manufacturer = models.CharField('Марка', max_length=200,)
    model = models.CharField('Модель', max_length=200,)
    color = models.CharField('Цвет', max_length=200,)
    plate_number = models.CharField(
        'Регистрационный номер',
        max_length=200,
        unique=True,
        null=False,
        validators=[RegexValidator(r'^[A-Z0-9\s]+$', message= 'Только заглавные латинские буквы и цифры')]

        )
    production_year = models.PositiveIntegerField(
        'Год выпуска',
        default=current_year(),
        validators=[MinValueValidator(1984), max_value_current_year]
        )
    vin = models.CharField(
        max_length=200,
        unique=True,
        null=False,
        validators=[RegexValidator(r'^[A-Z0-9]+$', message= 'Только заглавные латинские буквы и цифры')]
        )
    certificate_id = models.CharField(
        'Номер СТС (свидетельство о регистрации)',
        max_length=200, unique=True, null=False,
        validators=[RegexValidator(r'^[А-ЯA-Z0-9\s№]+$')]
        )
    certificate_year = models.PositiveIntegerField(
        'Дата СТС',
        default=current_year(),
        validators=[MinValueValidator(1984), max_value_current_year]
        )

    class Meta:
         verbose_name = 'Транспортное средство'
         verbose_name_plural = 'Транспортные средства'



    def __str__(self):
        return f'{self.manufacturer} {self.model}'
 
    