from django.contrib import messages
from . models import *
from django.views.decorators.csrf  import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from dashboard.models import Staff_UserAuth 
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import default_storage

def d_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Staff_UserAuth.objects.get(email=email)
        except Staff_UserAuth.DoesNotExist:
            user = None
        if user is not None:
            
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in!')
                return redirect('add_appartment')
            else:
                messages.error(request, 'Invalid password!')
        else:
            messages.error(request, 'Invalid email or user does not exist!')

        return render(request, 'dashboard/d_login.html')

    return render(request, 'dashboard/d_login.html')


@login_required(login_url='d_login')  
def d_logout(request):
    """
    Handle user logout
    """
    logout(request)  
    messages.success(request, 'Successfully logged out!')  
    return redirect('home')  

@login_required(login_url='d_login')  
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
        sqft_price = request.POST.get('sqft_price')
        total_price = request.POST.get('total_price')
        
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
            sqft_price=sqft_price,
            total_price=total_price
            
        )

        images = request.FILES.getlist('propertyimages') 
 
        for image in images:
            new_image = AppartmentImage.objects.create(image=image)
            apartment.images.add(new_image) 

        messages.success(request, "Apartment created successfully!")
        return redirect ('add_appartment')
    return render(request,'dashboard/add_appartment.html')


def list_apartments(request):
    apartments = Appartment.objects.prefetch_related('images').all()
    return render(request, 'dashboard/table.html', {'apartments': apartments})

def delete_apartment(request, apartment_id):
    apartment = get_object_or_404(Appartment, id=apartment_id)
    apartment.delete()
    messages.success(request, "Apartment deleted successfully!")
    return redirect('appartments')

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
        total_price = request.POST.get('total_price')
        total_sqft = request.POST.get('total_sqft')
        
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
            total_price=total_price,
            total_sqft=total_sqft

            
        )

        images = request.FILES.getlist('propertyimages') 
 
        for image in images:
            new_image = PlotImage.objects.create(image=image)
            plot.images.add(new_image)  

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
        sqft_price = request.POST.get('sqft_price')
        total_price = request.POST.get('total_price')
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
            sqft_price=sqft_price,
            total_price=total_price,
            
        )

        images = request.FILES.getlist('propertyimages')
 
        for image in images:
            new_image = CommercialImage.objects.create(image=image)
            commercial.images.add(new_image)  

        messages.success(request, "Commercial created successfully!")
        return redirect ('add_commercial')
    return render(request,'dashboard/add_commercial.html')


def appartments(request):
    if request.method == 'POST':
        property_type = request.POST.get('property_type', 'New')  
        appartments = Appartment.objects.filter(
            appartment_type="Appartment", property_type=property_type
        ).order_by('-created_at')
    else:
        property_type = 'New, ReSale'
        appartments = Appartment.objects.filter(
            appartment_type="Appartment", property_type__in=['New', 'ReSale']
        ).order_by('-created_at')

    return render(
        request,
        'dashboard/appartments.html',
        {"appartments": appartments, "property_type": property_type}
    )

def villas(request):
    if request.method == 'POST':
        property_type = request.POST.get('property_type', 'New')  
        villas = Appartment.objects.filter(
            appartment_type="Villa", property_type=property_type
        ).order_by('-created_at')
    else:
        property_type = 'New, ReSale'
        villas = Appartment.objects.filter(
            appartment_type="Villa", property_type__in=['New', 'ReSale']
        ).order_by('-created_at')

    return render(
        request,
        'dashboard/villas.html',
        {"villas": villas, "property_type": property_type}
    )

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

@csrf_exempt
def edit_apartment(request, apartment_id):
    apartment = get_object_or_404(Appartment, id=apartment_id)

    if request.method == 'POST':
        apartment.appartment_type = request.POST.get('appartment_type')
        apartment.project_name = request.POST.get('project_name')
        apartment.title = request.POST.get('title')
        apartment.description = request.POST.get('description')
        apartment.bhk = request.POST.get('bhk')
        apartment.bathrooms = request.POST.get('bathrooms')
        apartment.parking = request.POST.get('parking')
        apartment.floor_no = request.POST.get('floor_no')
        apartment.total_floors = request.POST.get('total_floors')
        apartment.maintenance = request.POST.get('maintenance')
        apartment.furnishing = request.POST.get('furnishing')
        apartment.land_area_sqft = request.POST.get('land_area_sqft')
        apartment.carpet_area_sqft = request.POST.get('carpet_area_sqft')
        apartment.area = request.POST.get('area')
        apartment.address = request.POST.get('address')
        apartment.nearby_school = request.POST.get('nearby_school')
        apartment.nearby_busortrain = request.POST.get('nearby_busortrain')
        apartment.facing = request.POST.get('facing_side')
        apartment.listed_by = request.POST.get('listed_by')
        apartment.property_type = request.POST.get('property_type')
        apartment.sqft_price =request.POST.get('sqft_price')
        apartment.total_price =request.POST.get('total_price')
        apartment.images.clear()

        if 'propertyimages' in request.FILES:
            images = request.FILES.getlist('propertyimages')
            for image in images:
                appartment_image = AppartmentImage.objects.create(image=image)
                apartment.images.add(appartment_image)

        apartment.save()

        messages.success(request, "Apartment updated successfully!")

        if apartment.appartment_type == 'Villa':
            return redirect('villas')  
        else:
            return redirect('appartments')  

    return render(request, 'dashboard/edit_apartment.html', {'apartment': apartment})



@csrf_exempt
def edit_plot(request, plot_id):
    plot = get_object_or_404(Plot, id=plot_id)
    if request.method == 'POST':
        plot.project_name = request.POST.get('project_name')
        plot.title = request.POST.get('title')
        plot.description = request.POST.get('description')
        plot.sqft = request.POST.get('sqft')
        plot.area = request.POST.get('area')
        plot.address = request.POST.get('address')
        plot.nearby_school = request.POST.get('nearby_school')
        plot.nearby_busortrain = request.POST.get('nearby_busortrain')
        plot.length = request.POST.get('length')
        plot.breadth = request.POST.get('breadth')
        plot.facing = request.POST.get('facing_side')
        plot.listed_by = request.POST.get('listed_by')
        plot.property_type = request.POST.get('property_type')
        plot.total_sqft = request.POST.get('total_sqft')
        plot.total_price = request.POST.get('total_price')
        plot.save()  

        plot.images.clear()

        
        images = request.FILES.getlist('propertyimages')
        for image in images:
            new_image = PlotImage.objects.create(image=image)
            plot.images.add(new_image)  

        messages.success(request, "Plot updated successfully!")
        return redirect('plots')

    return render(request, 'dashboard/edit_plot.html', {'plot': plot})
                  

@csrf_exempt
def delete_plot(request, plot_id):
    plot = get_object_or_404(Plot, id=plot_id)
    plot.delete()  
    messages.success(request, "Plot deleted successfully!")
    return redirect('add_plot')  


@csrf_exempt
def edit_commercial(request, commercial_id):
    commercial = get_object_or_404(Commercial, id=commercial_id)
    
    if request.method == 'POST':
        commercial.project_name = request.POST.get('project_name')
        commercial.title = request.POST.get('title')
        commercial.description = request.POST.get('description')
        commercial.washrooms = request.POST.get('washrooms')
        commercial.parking = request.POST.get('parking')
        commercial.floor_no = request.POST.get('floor_no')
        commercial.total_floors = request.POST.get('total_floors')
        commercial.maintenance = request.POST.get('maintenance')
        commercial.furnishing = request.POST.get('furnishing')
        commercial.super_area_sqft = request.POST.get('super_area_sqft')
        commercial.carpet_area_sqft = request.POST.get('carpet_area_sqft')
        commercial.area = request.POST.get('area')
        commercial.address = request.POST.get('address')
        commercial.nearby_school = request.POST.get('nearby_school')
        commercial.nearby_busortrain = request.POST.get('nearby_busortrain')
        commercial.facing = request.POST.get('facing_side')
        commercial.listed_by = request.POST.get('listed_by')
        commercial.property_type = request.POST.get('property_type')
        commercial.total_price = request.POST.get('total_price')
        commercial.sqft_price = request.POST.get('sqft_price')
        commercial.save() 
        commercial.images.clear()
        images = request.FILES.getlist('propertyimages')
        for image in images:
            new_image = CommercialImage.objects.create(image=image)
            commercial.images.add(new_image)  

        messages.success(request, "Commercial updated successfully!")
        return redirect('commercials')

    return render(request, 'dashboard/edit_commercial.html', {'commercial': commercial})


@csrf_exempt
def delete_commercial(request, commercial_id):
    commercial = get_object_or_404(Commercial, id=commercial_id)
    
    if request.method == 'POST':
        commercial.delete()
        messages.success(request, "Commercial deleted successfully!")
        return redirect('commercial_list')  

    return render(request, 'dashboard/delete_commercial.html', {'commercial': commercial})


@csrf_exempt
def d_contact(request):
    contacts = Contact.objects.all() 
    print(contacts)
    context = {
        'contacts': contacts
    }
    return render(request, 'dashboard/d_contact.html', context)


def d_gallery(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        reviews = request.POST.get('reviews')
        print(customer_name)
        customer_images = request.FILES.get('customer_images')

        if customer_name and customer_name and customer_images:

            gallerys = Gallery.objects.create(
                customer_name=customer_name,
                reviews=reviews,
                customer_images=customer_images

            ).save()
            messages.success(request, "gallery created successfully.")
            return redirect('d_gallery')
        else:

            messages.error(request, "customer_name, reviews,customer_images,are required.")
    gallerys = Gallery.objects.all()
    return render(request, 'dashboard/d_gallery.html', {'gallerys': gallerys,})



def delete_gallery(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)
    gallery.delete()
    return redirect('d_gallery')

