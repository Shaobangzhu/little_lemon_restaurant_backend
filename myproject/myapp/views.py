from django.shortcuts import render
from .models import Menu

# Create your views here.
def about(request):
    about_content = {'about': "Based in Chicago, Illinois, Little Lemon is a family owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12-15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, "about.html", about_content)

def menu(request):
    newmenu = {'mains': [
        {'name':"falafel", 'price': "12"},
        {'name':"shawama", 'price': "15"},
        {'name':"gyro", 'price': "10"},
        {'name':"humus", 'price': "5"},
    ]}
    return render(request, 'menu.html', newmenu)

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)