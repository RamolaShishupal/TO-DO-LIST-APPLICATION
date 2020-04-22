from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<note_id>',views.delete,name='delete'),
    path('update/<note_id>', views.update, name='update'),

]