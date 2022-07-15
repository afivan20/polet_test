from django.urls import path


from auto.views import AutoListCreate
from auto.views import AutoDetail, DownloadData

urlpatterns = [
    path('cars/', AutoListCreate.as_view()),
    path('cars/download/', DownloadData.as_view()),
    path('cars/<int:pk>/', AutoDetail.as_view()),
] 