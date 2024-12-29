from django.shortcuts import render
from . models import *
from dashboard.models import *
def home(request):
    return render(request,'website/index_slider.html')

def about(request):
    return render(request,'website/about.html')

def error(request):
    return render(request,'website/404.html')

def agencies_single(request):
    return render(request,'website/agencies_single.html')

def agencies(request):
    return render(request,'website/agencies.html')

def agents_single(request):
    return render(request,'website/agents_single.html')

def agents(request):
    return render(request,'website/agents.html')

def blog_grid(request):
    return render(request,'website/blog_grid.html')

def blog_list(request):
    return render(request,'website/blog_list.html')

def blog_single(request):
    return render(request,'website/blog_single.html')

def blog(request):
    return render(request,'website/blog.html')

def contact(request):
    return render(request,'website/contact.html')

def faqs(request):
    return render(request,'website/faqs.html')

def index_map(request):
    return render(request,'website/index_map.html')

def index_slider(request):
    return render(request,'website/index_slider.html')

def index_video(request):
    return render(request,'website/index_video.html')

def index(request):
    return render(request,'website/index.html')

def login(request):
    return render(request,'website/login.html')

def pricing(request):
    return render(request,'website/pricing.html')

def property_grid(request):
    return render(request,'website/property_grid.html')

def property_list(request):
    return render(request,'website/property_list.html')

def property_map(request):
    return render(request,'website/property_map.html')

def property_single(request):
    return render(request,'website/property_single.html')

def register(request):
    return render(request,'website/register.html')

def submit_property(request):
    return render(request,'website/submit_property.html')

def team(request):
    return render(request,'website/team.html')

def testimonials(request):
    return render(request,'website/testimonials.html')

def typography(request):
    return render(request,'website/typography.html')

def plots_properties(request):
    plots = Plot.objects.filter(property_type="New")
    return render(request,'website/plots.html',{"plots":plots})

def commercial_properties(request):
    commercials = Commercial.objects.filter(property_type="New")
    return render(request,'website/commercial_properties.html',{"commercials":commercials})

def appartments_properties(request):
    appartments = Appartment.objects.filter(appartment_type="Appartment",property_type="New").order_by('-created_at')
    return render(request,'website/appartments_properties.html',{"appartments":appartments})

def villas_properties(request):
    villas = Appartment.objects.filter(appartment_type="Villa",property_type="New").order_by('-created_at')
    return render(request,'website/villas_properties.html',{"villas":villas})

def apartments(request):
    return render(request,'website/apartments.html')

def individual_villa(request):
    return render(request,'website/individual_villa.html')
def comercial_property(request):
    return render(request,'website/comercial_property.html')

def resale_plots(request):
    resale_plots = Plot.objects.filter(property_type="ReSale")
    return render(request,'website/resale_plots.html',{"resale_plots":resale_plots})

def resale_comercial(request):
    resale_comercials = Commercial.objects.filter(property_type="ReSale")
    return render(request,'website/resale_plots.html',{"resale_comercials":resale_comercials})

def resale_apartments(request):
    resale_apartments = Appartment.objects.filter(appartment_type="Appartment",property_type="ReSale").order_by('-created_at')
    return render(request,'website/resale_apartments.html',{"resale_apartments":resale_apartments})

def resale_individual_villa(request):
    resale_villas = Appartment.objects.filter(appartment_type="Villa",property_type="ReSale").order_by('-created_at')
    return render(request,'website/resale_villas.html',{"resale_villas":resale_villas})