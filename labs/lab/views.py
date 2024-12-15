from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import requests
import urllib.parse

# Create your views here.

def index(request):
  return render(request, "lab/index.html")

def greetings(request):
  return HttpResponse("<h1>Hello World! Gurkirat Singh - N01604571</h1>")

def current_datetime(request):
  now = datetime.datetime.now()
  formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
  return HttpResponse(f"<h1>Current Date and Time: {formatted_now}</h1>")

def xkcd(request):
  if request.method == 'POST':
    comic_id = request.POST.get('comic_id')
    url = f"https://xkcd.com/{comic_id}/info.0.json"
    response = requests.get(url)
    comic_data = response.json()
    context = {
      'comic_id': comic_data['num'],
      'title': comic_data['title'],
      'year': comic_data['year']
      }
    return render(request, 'lab/get_xkcd.html', context)
  elif request.method == 'GET':
    return render(request, 'lab/xkcd.html')
  else:
    return HttpResponse("Invalid request method.")
  
def random_dog(request):
  url = "https://dog.ceo/api/breeds/image/random"
  response = requests.get(url)
  dog_data = response.json()
  context = {
    'image_url': dog_data['message'],
    'status': dog_data['status']
  }
  return render(request, 'lab/random_dog.html', context)

def get_dog(request):
  if request.method == 'POST':
    breed = request.POST.get('breed')
    url = f"https://dog.ceo/api/breed/{breed}/images/random/3 Fetch!"
    response = requests.get(url)
    dog_data = response.json()
    context = {
      'breed': breed,
      'images': dog_data['message'],
      'status': dog_data['status']
    }
    return render(request, 'lab/get_dog.html', context)
  else:
    return render(request, 'lab/get_dog.html')

def generate_qr_code(request):
  if request.method == 'POST':
    data = request.POST.get('data')
    encoded_data = urllib.parse.quote(data)
    qr_code_url = f"https://image-charts.com/chart?chs=150x150&cht=qr&chl={encoded_data}&choe=UTF-8"
    context = {
      'qr_code_url': qr_code_url,
      'data': data
    }
    return render(request, 'lab/generate_qr_code.html', context)
  else:
    return render(request, 'lab/generate_qr_code.html')