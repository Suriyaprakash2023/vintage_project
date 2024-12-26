from django.shortcuts import render
from . models import *

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

def plots(request):
    return render(request,'website/plots.html')

def apartments(request):
    return render(request,'website/apartments.html')

def individual_villa(request):
    return render(request,'website/individual_villa.html')
def comercial_property(request):
    return render(request,'website/comercial_property.html')

def resale_plots(request):
    return render(request,'website/resale_plots.html')

def resale_apartments(request):
    return render(request,'website/resale_apartments.html')

def resale_individual_villa(request):
    return render(request,'website/resale_individual_villa.html')