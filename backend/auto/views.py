from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from auto.models import Auto
from auto.serializers import AutoSerializer
from rest_framework.views import APIView
import csv
from rest_framework import filters


class AutoListCreate(ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^manufacturer', '^model', 'plate_number', '^vin', 'certificate_id', '=production_year',) 

class AutoDetail(RetrieveUpdateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer 

class DownloadData(APIView):
    def get(self, request):
        auto_list = Auto.objects.all()
        response = HttpResponse()
        response['Content-Disposition'] = 'attachment; filename=cars.csv'
        response['Content-type'] = 'application/csv; charset=utf-8'
        writer = csv.writer(response)
        writer.writerow([u'Марка', 'Модель', 'Цвет', 'Рег-ый номер', 'Год выпуска', 'Vin', 'Номер СТС', 'Дата СТС'])
        for auto in auto_list:
            writer.writerow(
            [
            auto.manufacturer, auto.model, auto.color,
            auto.plate_number, auto.production_year,
            auto.vin, auto.certificate_id, auto.certificate_year
            ]
            )

        return response


