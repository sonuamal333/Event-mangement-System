from django.db import models
import uuid

class Baseclass(models.Model):
    
    uuid = models.SlugField(unique=True, default=uuid.uuid4)
    
    active_status = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True) 
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Event(Baseclass): 
    
    id = models.CharField(max_length=10, primary_key=True)  # Your custom PK
    
    name = models.CharField(max_length=30)
    
    date = models.DateField(auto_now_add=True)
    
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Participant(Baseclass):
    
    id = models.CharField(max_length=10, primary_key=True)  # Your custom PK   
    
    name = models.CharField(max_length=50)
    
    email = models.EmailField(unique=True)
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
