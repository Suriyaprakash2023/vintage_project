from django.db import models


class Amenity(models.Model):
    AMENITY_TYPES = [
        ('college', 'College'),
        ('school', 'School'),
        ('hospital', 'Hospital'),
        ('industry', 'Industry'),
        ('eatout', 'Eat Out'),
        ('gov_office', 'Government Office'),
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=AMENITY_TYPES)
    address = models.TextField()
    distance_from_property = models.FloatField(help_text="Distance in kilometers")

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class PropertyImage(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.title}"


class PropertyDocument(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='property_documents/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Document for {self.property.title} - {self.description}"


# Updated Property model
class Property(models.Model):
    CATEGORY_CHOICES = [
        ('commercial', 'Commercial Property'),
        ('acres', 'Acres/Cents'),
        ('villa', 'Individual Villa'),
        ('resale_home', 'Resale Home'),
        ('resale_apartment', 'Resale Apartment'),
        ('new_apartment', 'New Apartment'),
        ('ongoing_project', 'Ongoing Project'),
        ('upcoming_project', 'Upcoming Project'),
        ('completed_project', 'Completed Project'),
        ('construction_project', 'Construction Project'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    area = models.FloatField(help_text="Area in square feet or acres")
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    nearby_amenities = models.ManyToManyField(Amenity, related_name='properties', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']

