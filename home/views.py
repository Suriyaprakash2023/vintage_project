from django.shortcuts import render
from . models import *
from dashboard.models import *
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf  import csrf_exempt

@csrf_exempt
def home(request):
    appartments = Appartment.objects.filter(appartment_type="Appartment", property_type="New").order_by('-created_at')[:3]
    plots = Plot.objects.filter(property_type="New")[:3]
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5]  # Removed villa_id exclusion
    resale_apartments = Appartment.objects.filter(
        appartment_type="Appartment",
        property_type="ReSale"
    ).order_by('-created_at')[:3]

    return render(request, 'website/index_slider.html', {
        "appartments": appartments,
        "plots": plots,
        "resale_apartments": resale_apartments,
        "recent_villas": recent_villas
    })


@csrf_exempt
def about(request):
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    return render(request,'website/about.html',{"recent_villas":recent_villas})

@csrf_exempt
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

def apartments(request):
    return render(request,'website/apartments.html')

def individual_villa(request):
    return render(request,'website/individual_villa.html')

def comercial_property(request):
    return render(request,'website/comercial_property.html')

@csrf_exempt
def plots_properties(request):
    plots = Plot.objects.filter(property_type="New")
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    return render(request,'website/plots.html',{"plots":plots,"recent_villas":recent_villas})

@csrf_exempt
def appartments_properties(request):
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    appartments = Appartment.objects.filter(appartment_type="Appartment",property_type="New").order_by('-created_at')
    return render(request,'website/appartments_properties.html',{"appartments":appartments,"recent_villas":recent_villas})

@csrf_exempt
def appartment_details(request, appartment_id):
    appartment = get_object_or_404(
        Appartment, 
        pk=appartment_id, 
        appartment_type="Appartment",  
        property_type="New"            
    )

    recent_appartments = Appartment.objects.filter(
        appartment_type="Appartment",  
        property_type="New"            
    ).exclude(id=appartment_id).order_by('-created_at')[:5]
    
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 

    return render(request, 'website/appartment_details.html', {
        'appartment': appartment,
        'recent_appartments': recent_appartments,
        "recent_villas":recent_villas  
    })


@csrf_exempt
def plot_details(request, plot_id):
    plot = get_object_or_404(Plot, pk=plot_id, property_type='New')
    recent_plots = Plot.objects.filter(property_type='New').exclude(id=plot_id).order_by('-created_at')[:5]
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    plots = [plot]
    return render(request, 'website/property_single.html', {'plots': plots, 'recent_events': recent_plots,"recent_villas":recent_villas})

@csrf_exempt
def commercial_properties(request):
    commercials = Commercial.objects.filter(property_type="New")
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    print(f"Fetched commercials: {commercials}")  
    return render(request, 'website/commercial_properties.html', {"commercials": commercials,"recent_villas":recent_villas})

@csrf_exempt
def commercial_details(request, commercial_id):
    commercial = get_object_or_404(Commercial, pk=commercial_id, property_type='New')
    recent_commercials = Commercial.objects.filter(property_type='New').exclude(id=commercial_id).order_by('-created_at')[:5]
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    return render(request, 'website/commercial_details.html', {
        'commercial': commercial,
        'recent_commercials': recent_commercials,
        "recent_villas":recent_villas
    })


@csrf_exempt
def villas_properties(request):
    villas = Appartment.objects.filter(appartment_type="Villa", property_type="New").order_by('-created_at')
    recent_appartments = Appartment.objects.filter(
    property_type='New'
    ).exclude(appartment_type="Villa").order_by('-created_at')[:5]
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 

    return render(request, 'website/villas_properties.html', {
        "villas": villas,
        "recent_appartments": recent_appartments,
        "recent_villas":recent_villas
    })



@csrf_exempt
def villa_details(request, villa_id):
    villa = get_object_or_404(Appartment, pk=villa_id, appartment_type="Villa", property_type="New")
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).exclude(id=villa_id).order_by('-created_at')[:5]
    return render(request, 'website/villa_details.html', {
        'villa': villa,
        'recent_villas': recent_villas  
    })



@csrf_exempt
def resale_plots(request):
    resale_plots = Plot.objects.filter(property_type="ReSale")
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    return render(request, 'website/resale_plots.html', {"resale_plots": resale_plots,"recent_villas":recent_villas})


@csrf_exempt
def resale_plot_details(request, plot_id):
    plot = get_object_or_404(Plot, pk=plot_id, property_type='ReSale')
    recent_plots = Plot.objects.filter(property_type='ReSale').exclude(id=plot_id).order_by('-created_at')[:5]
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    plots = [plot]
    return render(request, 'website/resale_plot_details.html', {'plots': plots, 'recent_plots': recent_plots,"recent_villas":recent_villas})


@csrf_exempt
def resale_comercial(request):
    resale_comercials = Commercial.objects.filter(property_type="ReSale")
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    print(resale_comercials)
    return render(request,'website/resale_commercials.html',{"resale_comercials":resale_comercials,"recent_villas":recent_villas})


@csrf_exempt
def resale_commercial_details(request, commercial_id):
    commercial = get_object_or_404(Commercial, pk=commercial_id, property_type='ReSale')
    recent_commercials = Commercial.objects.filter(property_type='ReSale').exclude(id=commercial_id).order_by('-created_at')[:5]
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    return render(request, 'website/resale_commercial_details.html', {
        'commercial': commercial,
        'recent_commercials': recent_commercials,
        "recent_villas":recent_villas
    })


@csrf_exempt
def resale_apartments(request):
    resale_apartments = Appartment.objects.filter(
        appartment_type="Appartment",
        property_type="ReSale"
    ).exclude(id__isnull=True).order_by('-created_at')
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5]   
    print(resale_apartments) 
    return render(request, 'website/resale_apartments.html', {"resale_apartments": resale_apartments,"recent_villas":recent_villas})


@csrf_exempt
def resale_appartment_details(request, appartment_id):
    appartment = get_object_or_404(Appartment, pk=appartment_id, property_type='ReSale')
    resale_recent_appartments = Appartment.objects.filter(
    appartment_type="Appartment", 
    property_type="ReSale"        
    ).exclude(id=appartment_id).order_by('-created_at')[:5]
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 

    
    return render(request, 'website/resale_appartment_details.html', {
        'appartment': appartment,
        'resale_recent_appartments': resale_recent_appartments,
        "recent_villas":recent_villas  
    })

@csrf_exempt
def resale_individual_villa(request):
    resale_villas = Appartment.objects.filter(appartment_type="Villa",property_type="ReSale").order_by('-created_at')
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    return render(request,'website/resale_villas.html',{"resale_villas":resale_villas,"recent_villas":recent_villas})

@csrf_exempt
def resale_villa_details(request, villa_id):
    villa = get_object_or_404(Appartment, pk=villa_id, appartment_type="Villa", property_type="ReSale")
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="ReSale"
    ).exclude(id=villa_id).order_by('-created_at')[:5]
   
    return render(request, 'website/resale_villa_details.html', {
        'villa': villa,
        'recent_villas': recent_villas  
    })
from django.shortcuts import render, redirect

@csrf_exempt
def contact(request):
    
    
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and phone and message: 
            contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
            contact.save()
            return redirect('contact')
        
          

    contacts = Contact.objects.all()
    return render(request, 'website/contact.html', {'contacts': contacts,"recent_villas":recent_villas})


@csrf_exempt
def gallery(request):
    galleries = Gallery.objects.all() 
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5]  
    return render(request, 'website/gallery.html', {'galleries': galleries,"recent_villas":recent_villas})

@csrf_exempt
def construction(request):
    recent_villas = Appartment.objects.filter(
        appartment_type="Villa", 
        property_type="New"
    ).order_by('-created_at')[:5] 
    return render(request,'website/construction.html',{"recent_villas":recent_villas})
