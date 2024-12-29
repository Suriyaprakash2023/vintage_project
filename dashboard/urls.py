from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='dashboard_index'), 
    path('add_appartment/', views.add_appartment, name='add_appartment'), 
    path('add_plot/', views.add_plot, name='add_plot'), 
    path('add_commercial/', views.add_commercial, name='add_commercial'), 
    path('appartments/', views.appartments, name='appartments'), 
    path('villas/', views.villas, name='villas'), 
    path('plots/', views.plots, name='plots'), 
    path('commercials/', views.commercials, name='commercials'), 
    path('table/',views.table,name='table'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

