from django.shortcuts import render
from .models import Menu


def menu(request):
    try:
        obj1 = Menu.objects.filter(category_id=1)
        obj2 = Menu.objects.filter(category_id=2)
        obj3 = Menu.objects.filter(category_id=3)

        return render(request, 'menu.html', {'obj1': obj1, 'obj2': obj2, 'obj3': obj3})
    except:
        return render(request, 'menu.html', {'obj1': obj1, 'obj2': obj2, 'obj3': obj3})
