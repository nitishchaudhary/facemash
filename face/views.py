from django.shortcuts import render , redirect
from .models import facemash
from django.http import HttpResponse
import random
import os

# Create your views here.

path = "c:/Users/Nitish/Desktop/Django/Facemash/media/pics"

def index(request):

    files = os.listdir(path)
    d =random.choice(files)
    e =random.choice(files)

    object1 = facemash.objects.get(img = 'pics/'+d)
    object2 = facemash.objects.get(img = 'pics/'+e)
    rating1 = object1.rating
    rating2 = object2.rating

    image2 ="media/pics/"+d
    image1 = "media/pics/"+e
    return render(request , 'index.html' , { 'image1':image1 , 'image2':image2})

def change_image1(request):
 
    files = os.listdir(path)
    d =random.choice(files)
    e =random.choice(files)
    object1 = facemash.objects.get(img = 'pics/'+d)
    object1.rating += 1
    object1.save()  
    image1 = "media/pics/"+d
    image2 ="media/pics/"+e
   
    return render(request , 'index.html' , {'image1':image1 , 'image2':image2 ,'object1':object1 })

def change_image2(request):
    files = os.listdir(path)
    d =random.choice(files)
    e =random.choice(files)
    object2 = facemash.objects.get(img = 'pics/'+e)
    object2.rating += 1
    object2.save() 
    image1 = "media/pics/"+d
    image2 ="media/pics/"+e
   
    return render(request , 'index.html' , {'image1':image1 , 'image2':image2})

def ranking(request):
    objects = facemash.objects.order_by('-rating')
    print(objects)
    length = objects.count()    
    return render(request , 'ranking.html' , {'objects':objects} )
