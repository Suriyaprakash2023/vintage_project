from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='dashboard_index'), 
    path('add_property', views.add_property, name='add_property'), 
    path('properties', views.properties, name='properties'), 
    path('table/',views.table,name='table'),
    path('plot_dashboard/',views.plot_dashboard,name='plot_dashboard'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

