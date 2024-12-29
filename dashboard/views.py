from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
from django.views.decorators.csrf  import csrf_exempt

def index(request):
    return render(request,'dashboard/index.html')

@csrf_exempt
def add_appartment(request):
    if request.method == 'POST':

        appartment_type = request.POST.get('appartment_type')
        project_name = request.POST.get('project_name')
        title = request.POST.get('title')
        description = request.POST.get('description')
        bhk = request.POST.get('bhk')
        bathrooms = request.POST.get('bathrooms')
        parking = request.POST.get('parking')
        floor_no = request.POST.get('floor_no')
        total_floors = request.POST.get('total_floors')
        maintenance = request.POST.get('maintenance')
        furnishing = request.POST.get('furnishing')
        land_area_sqft = request.POST.get('land_area_sqft')
        carpet_area_sqft = request.POST.get('carpet_area_sqft')
        area = request.POST.get('area')
        address = request.POST.get('address')
        nearby_school = request.POST.get('nearby_school')
        nearby_busortrain = request.POST.get('nearby_busortrain')
        facing = request.POST.get('facing_side')
        listed_by = request.POST.get('listed_by')
        property_type = request.POST.get('property_type')
        
        print(description,"description")
        apartment = Appartment.objects.create(
            appartment_type = appartment_type ,
            project_name=project_name,
            title=title,
            description=description,
            bhk=bhk,
            bathrooms=bathrooms,
            parking=parking,
            floor_no=floor_no,
            total_floors=total_floors,
            maintenance=maintenance,
            furnishing=furnishing,
            land_area_sqft=land_area_sqft,
            carpet_area_sqft=carpet_area_sqft,
            area=area,
            address=address,
            nearby_school=nearby_school,
            nearby_busortrain=nearby_busortrain,
            facing=facing,
            listed_by=listed_by,
            property_type=property_type,
            
        )

        images = request.FILES.getlist('propertyimages') # Get all uploaded files
 
        for image in images:
            new_image = AppartmentImage.objects.create(image=image)
            apartment.images.add(new_image)  # Associate image with apartment

        messages.success(request, "Apartment created successfully!")
        return redirect ('add_appartment')
    return render(request,'dashboard/add_appartment.html')

@csrf_exempt
def add_plot(request):
    if request.method == 'POST':

        project_name = request.POST.get('project_name')
        title = request.POST.get('title')
        description = request.POST.get('description')
        sqft = request.POST.get('sqft')
        area = request.POST.get('area')
        address = request.POST.get('address')
        nearby_school = request.POST.get('nearby_school')
        nearby_busortrain = request.POST.get('nearby_busortrain')
        length = request.POST.get('length')
        breadth = request.POST.get('breadth')
        facing = request.POST.get('facing_side')
        listed_by = request.POST.get('listed_by')
        property_type = request.POST.get('property_type')
        
        print(description,"description")
        plot = Plot.objects.create(
            project_name=project_name,
            title=title,
            description=description,
            sqft=sqft,
            length=length,
            breadth=breadth,
            area=area,
            address=address,
            nearby_school=nearby_school,
            nearby_busortrain=nearby_busortrain,
            facing=facing,
            listed_by=listed_by,
            property_type=property_type,
            
        )

        images = request.FILES.getlist('propertyimages') # Get all uploaded files
 
        for image in images:
            new_image = PlotImage.objects.create(image=image)
            plot.images.add(new_image)  # Associate image with apartment

        messages.success(request, "Plot created successfully!")
        return redirect ('add_plot')
    return render(request,'dashboard/add_plot.html')

@csrf_exempt
def add_commercial(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        title = request.POST.get('title')
        description = request.POST.get('description')
        washrooms = request.POST.get('washrooms')
        parking = request.POST.get('parking')
        floor_no = request.POST.get('floor_no')
        total_floors = request.POST.get('total_floors')
        maintenance = request.POST.get('maintenance')
        furnishing = request.POST.get('furnishing')
        super_area_sqft = request.POST.get('super_area_sqft')
        carpet_area_sqft = request.POST.get('carpet_area_sqft')
        area = request.POST.get('area')
        address = request.POST.get('address')
        nearby_school = request.POST.get('nearby_school')
        nearby_busortrain = request.POST.get('nearby_busortrain')
        facing = request.POST.get('facing_side')
        listed_by = request.POST.get('listed_by')
        property_type = request.POST.get('property_type')
        
        print(description,"description")
        commercial = Commercial.objects.create(
            project_name=project_name,
            title=title,
            description=description,
            washrooms=washrooms,
            parking=parking,
            maintenance=maintenance,
            furnishing=furnishing,
            super_area_sqft=super_area_sqft,
            carpet_area_sqft=carpet_area_sqft,
            area=area,
            address=address,
            nearby_school=nearby_school,
            nearby_busortrain=nearby_busortrain,
            facing=facing,
            listed_by=listed_by,
            property_type=property_type,
            
        )

        images = request.FILES.getlist('propertyimages') # Get all uploaded files
 
        for image in images:
            new_image = CommercialImage.objects.create(image=image)
            commercial.images.add(new_image)  # Associate image with apartment

        messages.success(request, "Commercial created successfully!")
        return redirect ('add_commercial')
    return render(request,'dashboard/add_commercial.html')

def appartments(request):
    appartments = Appartment.objects.filter(appartment_type = "Appartment",property_type="New").order_by('-created_at')
    if request.method == 'POST':
        property_type = request.POST.get('property_type')
        appartments = Appartment.objects.filter(appartment_type = "Appartment",property_type=property_type).order_by('-created_at')
        return render(request,'dashboard/appartments.html',{"appartments":appartments})
    return render(request,'dashboard/appartments.html',{"appartments":appartments})

def villas(request):
    villas = Appartment.objects.filter(appartment_type = "Villa").order_by('-created_at')
    if request.method == 'POST':
        property_type = request.POST.get('property_type')
        villas = Appartment.objects.filter(appartment_type = "Villa",property_type=property_type).order_by('-created_at')
        return render(request,'dashboard/villas.html',{"villas":villas})
    return render(request,'dashboard/villas.html',{"villas":villas})



def plots(request):
    plots = Plot.objects.all().order_by('-created_at')
    if request.method == 'POST':
        property_type = request.POST.get('property_type')
        plots = Plot.objects.filter(property_type=property_type).order_by('-created_at')
        return render(request,'dashboard/plots.html',{"plots":plots})
    return render(request,'dashboard/plots.html',{"plots":plots})

def commercials(request):
    commercials = Commercial.objects.all().order_by('-created_at')
    if request.method == 'POST':
        property_type = request.POST.get('property_type')
        commercials = Commercial.objects.filter(property_type=property_type).order_by('-created_at')
        return render(request,'dashboard/commercials.html',{"commercials":commercials})
    return render(request,'dashboard/commercials.html',{"commercials":commercials})


def table(request):
    return render(request,'dashboard/table.html')
