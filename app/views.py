from django.shortcuts import render

# Create your views here.
def send_data(request):
    d={'name':'Manju','course':'Python','age':23}
    return render(request, 'send_data.html', context=d)
