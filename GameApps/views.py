from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponseRedirect

from .models import GameApp, ProducerCompany, Rule


from .models_1st import GameApp_1st

from Forum.models import  UserMember

from datetime import timedelta, datetime, date





def  display_available_games(request):

	qs = GameApp.objects.all()

	if request.user.is_authenticated:

		template_path = "GameApp/Games.html"

	else:

		template_path = "BASE.html"

	context = {'qs' : qs}

	return render(request, template_path, context)




def authors_view(request):
	
	#n=GameApp_1st.objects.all().count()
	#print(n)

    

    var = GameApp_1st()
    var1 = UserMember.objects.all()

    date1 = GameApp_1st.objects.get(pk=1).release
    date2 = date(2020,10,1)

    var.qs_date_count_1st = GameApp_1st.objects.get_time_frame(date1, date2)
    var.qs_date_count= GameApp_1st.objects.get_time_frame(date1, date2).count()

    print(var.qs_date_count_1st)
    print(var.qs_date_count)
    print(date1)
    print(date2)

    context = {'var' : var ,
    			'var1' : var1,}

    if request.user.is_authenticated:

    	template_path = "GameApp/authors-page.html"

    else:

    	template_path = "BASE.html"

    return render(request, template_path, context)





def display_rules(request):

    var = Rule()
    
    qs = Rule.objects.all()


    date1 = Rule.objects.get(pk=1).start_date
    date2 = date(2020,10,4)

    var.qs_date_count_1st = Rule.objects.get_time_frame(date1, date2)
    var.qs_date_count= Rule.objects.get_time_frame(date1, date2).count()
    var.qs_date_count_n = Rule.objects.get_time_frame(date1, date2)

    var.qs_date_count_active = Rule.objects.get_time_frame_active()
    var.qs_date_count_inactive = Rule.objects.get_time_frame_inactive()


    print(var.qs_date_count_1st)
    print(var.qs_date_count)
    print(var.qs_date_count_n)

    print(var.qs_date_count_active)
    print(var.qs_date_count_inactive)


    print(date1)
    print(date2)



    if request.user.is_authenticated:

        template_path = "GameApp/rules.html"

    else:

        template_path = "BASE.html"

    context = {"var": var,
                'qs' : qs}

    return render(request, template_path, context)






def display_app_to_rate(request, id):

    obj = GameApp.objects.get(id=id)

    if request.method== 'POST':
        if 'rate' in request.POST:
            obj.rating+=1
            obj.save()
            return redirect('authors')

        elif 'like' in request.POST:
            obj.likes+=1
            obj.save()
            return redirect('authors')



    if request.user.is_authenticated:

        template_path = "GameApp/game-app-rating.html"

    else:

        template_path = "BASE.html"

    context = {'obj' : obj}

    return render(request, template_path, context)





def display_apps_rating(request):

    qs = GameApp.objects.all()

    if request.user.is_authenticated:

        template_path = "GameApp/apps-rating.html"

    else:

        template_path = "BASE.html"

    context = {'qs' : qs}

    return render(request, template_path, context)

































