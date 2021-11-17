from django.urls import path
from . import views

urlpatterns = [
    path('',views.Baseview,name='home'),
    path('file/',views.uploadview,name='file'),
    path('newfile/',views.model_form_upload,name='newfile'),
    path('showfile/',views.showdataview,name='showfile'),
]