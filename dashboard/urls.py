from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.d_login, name='d_login'),
    path('d_logout/', views.d_logout, name='d_logout'),

    path('index', views.index, name='dashboard_index'), 
    path('add_appartment/', views.add_appartment, name='add_appartment'),

    path('add_plot/', views.add_plot, name='add_plot'), 
    path('plots/', views.plots, name='plots'), 
    path('edit_plot/<int:plot_id>/', views.edit_plot, name='edit_plot'),
    path('delete_plot/<int:plot_id>/', views.delete_plot, name='delete_plot'),

    path('commercials/', views.commercials, name='commercials'), 
    path('add_commercial/', views.add_commercial, name='add_commercial'),
    path('edit_commercial/<int:commercial_id>/', views.edit_commercial, name='edit_commercial'),
    path('delete_commercial/<int:commercial_id>/', views.delete_commercial, name='delete_commercial'), 

    path('appartments/', views.appartments, name='appartments'), 
    path('villas/', views.villas, name='villas'), 
    
    path('d_contact/',views.d_contact,name='d_contact'),
    path('d_gallery/',views.d_gallery,name='d_gallery'),
    path('delete_gallery/<int:gallery_id>/', views.delete_gallery, name='delete_gallery'),
    # path('add-apartment/', views.add_apartment, name='add_apartment'),

    path('list_apartments/', views.list_apartments, name='list_apartments'),
    path('apartments/edit/<int:apartment_id>/', views.edit_apartment, name='edit_apartment'),
    path('apartments/delete/<int:apartment_id>/', views.delete_apartment, name='delete_apartment'),
    path('edit_apartment/<int:apartment_id>/', views.edit_apartment, name='edit_apartment'),
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

