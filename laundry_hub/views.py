from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def services(request):
    our_services = ["Dry cleaner", "Ironing", "Carpet cleaning", "house cleaning", ]
    price = kilogram = 70
    opening = 7

    return render(request, 'services.html', {"services": our_services, 'price': price, 'opening': opening})


def about(request):
    return render(request, 'about.html')


def main(request):
    return render(request, 'main.html')
