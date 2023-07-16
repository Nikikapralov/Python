from django.shortcuts import render

# Create your views here.
def index_2(request):
    return render(request, 'secondary_app/Index_2.html')