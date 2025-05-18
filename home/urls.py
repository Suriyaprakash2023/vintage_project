from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.home,name="home"),
    path('404/', views.error, name='error'),
    path('agencies/', views.agencies, name='agencies'),
    path('about/', views.about, name='about'),
    path('agencies/single/', views.agencies_single, name='agencies_single'),
    path('agents/', views.agents, name='agents'),
    path('agents/single/', views.agents_single, name='agents_single'),
    path('blog/', views.blog, name='blog'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog/grid/', views.blog_grid, name='blog_grid'),
    path('blog/single/', views.blog_single, name='blog_single'),

    path('contact/', views.contact, name='contact'),
    path('construction/', views.construction, name='construction'),
    path('gallery/', views.gallery, name='gallery'),
    
    path('faqs/', views.faqs, name='faqs'),
    path('index/map/', views.index_map, name='index_map'),
    path('index/slider/', views.index_slider, name='index_slider'),
    path('index/video/', views.index_video, name='index_video'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('pricing/', views.pricing, name='pricing'),
    path('property/grid/', views.property_grid, name='property_grid'),
    path('property/list/', views.property_list, name='property_list'),
    path('property/map/', views.property_map, name='property_map'),
    path('property/single/', views.property_single, name='property_single'),
    path('register/', views.register, name='register'),
    path('submit-property/', views.submit_property, name='submit_property'),
    path('team/', views.team, name='team'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('typography/', views.typography, name='typography'),

    path('plots_properties/', views.plots_properties, name='plots_properties'),
    path('plot_details/<int:plot_id>/', views.plot_details, name='plot_details'),

    path('appartments_properties/', views.appartments_properties, name='appartments_properties'),
    path('appartment_details/<int:appartment_id>/', views.appartment_details, name='appartment_details'),

    path('villas_properties/', views.villas_properties, name='villas_properties'),
    path('villa_details/<int:villa_id>/', views.villa_details, name='villa_details'),

    path('commercial_properties/', views.commercial_properties, name='commercial_properties'),
    path('commercial_details/<int:commercial_id>/', views.commercial_details, name='commercial_details'),


    path('apartments/', views.apartments, name='apartments'),
    path('individual_villa/', views.individual_villa, name='individual_villa'),
    path('comercial_property/', views.comercial_property, name='comercial_property'),

    path('resale_plots/', views.resale_plots, name='resale_plots'),
    path('resale_plot_details/<int:plot_id>/', views.resale_plot_details, name='resale_plot_details'),

    
    path('resale_apartments/', views.resale_apartments, name='resale_apartments'),
    path('resale_appartment_details/<int:appartment_id>/', views.resale_appartment_details, name='resale_appartment_details'),


    path('resale_comercial/', views.resale_comercial, name='resale_comercial'),
    path('resale_commercial_details/<int:commercial_id>/', views.resale_commercial_details, name='resale_commercial_details'),

    path('resale_individual_villa/', views.resale_individual_villa, name='resale_individual_villa'),
    path('resale_villa_details/<int:villa_id>/', views.resale_villa_details, name='resale_villa_details'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)