import random
import string
from datetime import datetime
from django.contrib.auth.models import Group, AbstractUser
from django.db import models, connection
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class AlphaNumericFieldfour(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 4 
        super().__init__(*args, **kwargs)

    @staticmethod
    def generate_alphanumeric():
        alphanumeric = "".join(
            random.choices(string.ascii_letters + string.digits, k=4)
        )
        return alphanumeric.upper()


class AlphaNumericFieldfive(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 5  
        super().__init__(*args, **kwargs)

    @staticmethod
    def generate_alphanumeric():
        alphanumeric = "".join(
            random.choices(string.ascii_letters + string.digits, k=5)
        )
        return alphanumeric.upper()


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Staff_UserAuth(AbstractUser):
    
    objects = CustomUserManager()
    username = None
    last_name = None

    email = models.EmailField(_("email address"), unique=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    THMID = models.CharField(max_length=10, null=True, blank=True)
    referral_code = AlphaNumericFieldfive(unique=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = AlphaNumericFieldfive.generate_alphanumeric()
            while Staff_UserAuth.objects.filter(
                referral_code=self.referral_code
            ).exists():
                self.referral_code = AlphaNumericFieldfive.generate_alphanumeric()
        super(Staff_UserAuth, self).save(*args, **kwargs)




groups = [
    "User",
    "Admin",
   
 ]



@receiver(post_migrate)
def create_groups(sender, **kwargs):
    with connection.cursor() as cursor:
        table_names = connection.introspection.table_names(cursor)
        if "auth_group" in table_names:
            for group_name in groups:
                Group.objects.get_or_create(name=group_name)
        else:
            print("auth_group table does not exist, skipping group creation.")
 

PROPERTY_TYPES = [
    ('New', 'New'),
    ('ReSale', 'ReSale'),   
]
PROPERTY_CATEGORY = [
    ('Appartment', 'Appartment'),
    ('Villa', 'Villa'),   
]
LISTED_BY = [
    ('Builder', 'Builder'),
    ('Dealer', 'Dealer'),    
]
FURNISH_TYPE = [
    ('Furnished', 'Furnished'),
    ('Semi-Furnished', 'Semi-Furnished'),    
    ('UnFurnished', 'UnFurnished'),    
]
 
COMMERCIAL_TYPES = [
    ('Office', 'Office'),
    ('Shop', 'Shop'),
]

FACING_SIDE = [
    ('East', 'East'),
    ('West', 'West'),
    ('North', 'North'),
    ('South', 'South'),

]


# Define a generic Image model
class PlotImage(models.Model):
    image = models.ImageField(upload_to='plot_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
    
class AppartmentImage(models.Model):
    image = models.ImageField(upload_to='appartment_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
    
class CommercialImage(models.Model):
    image = models.ImageField(upload_to='commercial_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

# Plot model
class Plot(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    project_name = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=700, null=True, blank=True)
    sqft = models.CharField(max_length=10, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    nearby_school = models.CharField(max_length=100, null=True, blank=True)
    nearby_busortrain = models.CharField(max_length=100, null=True, blank=True)
    length = models.CharField(max_length=100, null=True, blank=True)
    breadth = models.CharField(max_length=100, null=True, blank=True)
    facing = models.CharField(choices=FACING_SIDE, max_length=30, null=True, blank=True)
    listed_by = models.CharField(choices=LISTED_BY, default='Builder', max_length=30)
    property_type = models.CharField(choices=PROPERTY_TYPES, max_length=30, null=True, blank=True)
    images = models.ManyToManyField(PlotImage, related_name="plot_images", blank=True)
    avaliable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# Appartment model
class Appartment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    project_name = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=700, null=True, blank=True)
    bhk = models.CharField(max_length=10, null=True, blank=True)
    bathrooms = models.CharField(max_length=10, null=True, blank=True)
    parking = models.CharField(max_length=10, null=True, blank=True)
    floor_no = models.CharField(max_length=10, null=True, blank=True)
    total_floors = models.CharField(max_length=10, null=True, blank=True)
    maintenance = models.CharField(max_length=10, null=True, blank=True)
    furnishing = models.CharField(max_length=20, choices=FURNISH_TYPE, null=True, blank=True)
    land_area_sqft = models.CharField(max_length=10, null=True, blank=True)
    carpet_area_sqft = models.CharField(max_length=10, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    nearby_school = models.CharField(max_length=100, null=True, blank=True)
    nearby_busortrain = models.CharField(max_length=100, null=True, blank=True)
    facing = models.CharField(choices=FACING_SIDE, max_length=30, null=True, blank=True)
    listed_by = models.CharField(choices=LISTED_BY, default='Builder', max_length=30, null=True, blank=True)
    property_type = models.CharField(choices=PROPERTY_TYPES, max_length=30, null=True, blank=True)
    appartment_type = models.CharField(choices=PROPERTY_CATEGORY, max_length=30, null=True, blank=True)
    images = models.ManyToManyField(AppartmentImage, related_name="appartment_images", blank=True)
    avaliable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Commercial model
class Commercial(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    project_name = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=700, null=True, blank=True)
    furnishing = models.CharField(max_length=20, choices=FURNISH_TYPE, null=True, blank=True)
    listed_by = models.CharField(max_length=10, choices=LISTED_BY, null=True, blank=True)
    super_area_sqft = models.CharField(max_length=10, null=True, blank=True)
    carpet_area_sqft = models.CharField(max_length=10, null=True, blank=True)
    maintenance = models.CharField(max_length=10, null=True, blank=True)
    facing = models.CharField(choices=FACING_SIDE, max_length=30, null=True, blank=True)
    parking = models.CharField(max_length=10, null=True, blank=True)
    washrooms = models.CharField(max_length=10, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    nearby_school = models.CharField(max_length=100, null=True, blank=True)
    nearby_busortrain = models.CharField(max_length=100, null=True, blank=True)
    images = models.ManyToManyField(CommercialImage, related_name="commercial_images", blank=True)
    avaliable = models.BooleanField(default=True)
    property_type = models.CharField(choices=PROPERTY_TYPES, max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title