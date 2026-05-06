from django.urls import path
from .views import *

urlpatterns = [
    path('', AdmissionListView.as_view(), name='list'),
    path('create/', AdmissionCreateView.as_view(), name='create'),
    path('update/<int:pk>', AdmissionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', AdmissionDeleteView.as_view(), name='delete'),
]
