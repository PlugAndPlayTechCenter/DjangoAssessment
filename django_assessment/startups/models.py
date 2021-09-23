from django.db import models

# Create your models here.
class Startup(models.Model):
    startup_name = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    one_liner = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    country = models.ForeignKey(
        'startups.Country', on_delete=models.SET_NULL, related_name='startups', null=True, blank=True) 
    city = models.CharField(max_length=100, null=True, blank=True)
    founded = models.CharField(max_length=30, null=True, blank=True)
    stage = models.ForeignKey('startups.Stage', on_delete=models.SET_NULL, null=True)
    money_raised_usd = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['website']

class StageManager(models.Manager):
    def get_by_natural_key(self, stage_name):
        return self.get(stage_name=stage_name)

class Stage(models.Model):
    stage_name = models.CharField(max_length=255,unique=True)
    objects = StageManager()

    def natural_key(self):
        return (self.stage_name,)
    
class CountryManager(models.Manager):
    def get_by_natural_key(self, country_code):
        return self.get(country_code=country_code)
    
class Country(models.Model):
    country_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=4, null=True, blank=True, unique=True)
    objects = CountryManager()
    def natural_key(self):
        return (self.country_code,)

class ContactManager(models.Manager):
    def get_by_natural_key(self, contact_email):
        return self.get(contact_email=contact_email)

class Contact(models.Model):
    contact_name = models.CharField(max_length=255)
    contact_position= models.CharField(max_length=128, null=True, blank=True)
    contact_email = models.EmailField(max_length=254, unique=True)
    startup = models.ForeignKey('startups.Startup', on_delete=models.CASCADE, null=True)
    objects = ContactManager()
    def natural_key(self):
        return (self.contact_email,)

class PrescriptorManager(models.Manager):
    def get_by_natural_key(self, prescriptor_email):
        return self.get(prescriptor_email=prescriptor_email)

class Prescriptor(models.Model):
    prescriptor_name = models.CharField(max_length=255)
    prescriptor_position= models.CharField(max_length=128, null=True, blank=True)
    prescriptor_email = models.EmailField(max_length=254,unique=True)
    company = models.CharField(max_length=128, null=True, blank=True)
    objects=PrescriptorManager()
    def natural_key(self):
        return (self.prescriptor_email,)
    
    