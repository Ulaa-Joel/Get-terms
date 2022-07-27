from django.shortcuts import render
from .models import Theme

# Create your views here.

def index(request):
    if Theme.object.filter(user=request.user.username).exists():
        color = Theme.objects.get(user=request.user.username).color
    else:
            color = 'blue'
    return render(request, 'index.html', {'color':color} )

def theme(request):
        color = request.GET.get('color')

        if color == 'dark':
            if Theme.object.filter(user=request.user.username).exists():
                user_theme = Theme.objects.get(user=request.user.username)
                user_theme.user = request.user.username
                user_theme.color = 'grey'
                user_theme.save()

            else:
                user2 = Theme(user=request.user.username, color='grey')
                user2.save()

        elif color == 'light':
            if Theme.object.filter(user=request.user.username).exists():
                user_theme1 = Theme.objects.get(user=request.user.username)
                user_theme1.user = request.user.username
                user_theme1.color = 'white'
                user_theme1.save()

            else:
                user4 = Theme(user=request.user.username, color='white')
                user4.save()

        #return redirect('/')
