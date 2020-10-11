from django.shortcuts import render, redirect



def welcome(request):
    if request.user.is_authenticated:
        return redirect('welcome_to_game_apps_view')
    else:
        return render(request, 'PLAYER/LOGIN_FORM.html')
