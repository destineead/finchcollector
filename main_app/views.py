from django.shortcuts import render

finches = [
  {'name': 'Stripes', 'breed': 'zebra finch', 'description': 'colorful with distinctive markings.', 'age': '2'},
  {'name': 'Shine', 'breed': 'gouldian finch', 'description': 'brightly colored with vibrant plumage.', 'age': '1'},
]
# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches' : finches
  })