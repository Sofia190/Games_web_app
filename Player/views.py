from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm



from django.conf import settings

from django.contrib.auth import get_user_model

from Forum.models import UserMember




User = settings.AUTH_USER_MODEL   #auth.User

   

def signup_function_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            form.save()
            usermember = UserMember()
            usermember.user = User.objects.last()
            print("Username", User.objects.last().get_username())
            usermember.save()
            return redirect('Game_apps_welcome')

    else:
        form = UserCreationForm()
        
    return render(request, 'PLAYER/SIGNUP_FORM.html', {'form': form})

