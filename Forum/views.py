

from django.shortcuts import render, redirect, get_object_or_404  #, login_required  


from django.contrib.auth import authenticate, login

from django.urls import reverse

from django.http import HttpResponseRedirect 

from django.http import HttpResponse, Http404




from .models import (Discussion, Email, Reply, UserMember, Reply_in_reply, 
 MailMessage)


from GameApps.models_1st import GameApp_1st


from . forms import  (MessageForm , PostForm , ReplyForm, Reply_in_reply_Form, 
	Create_user_profile_Form,
	SettingsForm, 
	SendMessageForm,
	AccountForm,)





from datetime import timedelta, datetime, date

from django.utils import timezone


from django.conf import settings

from django.contrib.auth import get_user_model


User = settings.AUTH_USER_MODEL   #auth.User




# Create your views here.


def welcome_to_game_apps_view(request):

	obj = UserMember.objects.all()


	if request.user.is_authenticated:

		template_path = "Forum/welcome-to-game-apps.html"

	else:

		template_path = "BASE.html"

	context = {"obj":obj, }

	return render(request, template_path, context)




def list_view(request):


    qs=Discussion.objects.all()

    context_dictionary = {"object_list" : qs,}

    if request.user.is_authenticated:

    	template_path = "Forum/discussion.html"
    else:
    	template_path = "BASE.html"

    return render(request, template_path, context_dictionary)






def detail_forum(request, id):

	try:
		qs = Discussion.objects.get(id=id)

	except:

		raise Http404


	qs1 =  Discussion.objects.get(id=id).d_replies.all()


	context_dictionary = {"object" : qs,
			     "qs1" : qs1,}

	if request.user.is_authenticated:

		template_path = "Forum/detail-forum.html"

	else:

		template_path = "BASE.html"


	return render(request, template_path, context_dictionary)





def view_replies_in_reply(request, id):



	qs1 =  Reply.objects.get(id=id).replies.all()

	print("Qs count =", qs1.count())


	context_dictionary = {
			     "qs1" : qs1,}
	

	if request.user.is_authenticated:

		template_path = "Forum/detail-forum-replies.html"

	else:

		template_path = "BASE.html"


	return render(request, template_path, context_dictionary)






def create_post(request):

	form = MessageForm(request.POST)

	if request.method == 'POST':

		if form.is_valid():
			form.save()
			print(request.user)
			var=Discussion.objects.last()
			var.user = request.user
			print(var.user)
			var.save()
			form = MessageForm()
			return redirect('list_view')

	else:
		form = MessageForm()

	
	context_dictionary = {'form' : form}

	if request.user.is_authenticated:
		template_path = "Forum/create-post.html"
	else:
		template_path = "BASE.html"

	return render(request, template_path, context_dictionary)






#@login_required
def update_post(request, id):

    obj=get_object_or_404(Discussion, id=id)

    form = PostForm(request.POST or None, instance=obj)

    context_dictionary = {'form' : form, }

    if form.is_valid():
    	obj=form.save()
    	obj.save()
    	return HttpResponseRedirect("/detail-forum/{id}".format(id=obj.id))

    if request.user.is_authenticated and (request.user == obj.user or request.user.is_staff):

    	template_path = "Forum/update-post.html"
    else:
    	template_path = "BASE.html"


    return render(request, template_path, context_dictionary)






def post_reply(request, id):

	form = ReplyForm(request.POST)

	discussion_instance = Discussion.objects.get(id=id)


	if request.method == 'POST':

		if form.is_valid():
			form.save()
			obj = Reply.objects.last()
			discussion_instance.d_replies.add(obj)	

			print(request.user)
			obj.user = request.user
			print(obj.user)
			obj.save()


			form = ReplyForm()
			return redirect('list_view')
	else:
		form = ReplyForm()

	

	context_dictionary = {'form' : form,}
	                      

	if request.user.is_authenticated:
		template_path = "Forum/post-reply.html"
	else:
		template_path = "BASE.html"

	return render(request, template_path, context_dictionary)






#@login_required
def update_reply(request, id):

    obj=get_object_or_404(Reply, id=id)

    form = ReplyForm(request.POST or None, instance=obj)

    context_dictionary = {'form' : form, }

    if form.is_valid():
    	obj=form.save()
    	obj.save()
    	return HttpResponseRedirect("/list-posts")



    if request.user.is_authenticated and request.user==obj.user:

    	template_path = "Forum/update-post-reply.html"
    else:
    	template_path = "BASE.html"


    return render(request, template_path, context_dictionary)






def my_view(request, id):
    
    obj = Discussion.objects.get(id=id)

    return HttpResponseRedirect("/update/{id}".format(id=obj.id))

	



def my_view1(request, id):
    
    obj = Discussion.objects.get(id=id)

    return HttpResponseRedirect("/reply/{id}".format(id=obj.id))

	




def user_profile_view(request,id):
    
    obj = get_object_or_404(UserMember, id=id)


    if (request.user.is_authenticated and obj.private == False and 
    	obj.display_picture == True):

    	template_path = "Forum/user-profile.html"

    elif (request.user.is_authenticated and obj.private==False and
    	obj.display_picture == False):

    	template_path = "Forum/user-profile-do-not-display-picture.html"


    elif request.user.is_authenticated and obj.private == True:

    	template_path = "Forum/this-profile-is-private.html"


    else:
    	template_path = "BASE.html"

    context = {'obj' : obj}
    return render(request, template_path, context)





def user_contribution_view(request, id):

	try:

		obj = UserMember.objects.get(id=id)

	except:

		raise Http404

	qs1 =  UserMember.objects.get(id=id).usermember_topics.all()


	context_dictionary = {"obj" : obj,
			     "qs1" : qs1,}



	if (request.user.is_authenticated and obj.display_topics == True and 
    	obj.display_picture == True):

		template_path = "Forum/user-contribution.html"

	elif (request.user.is_authenticated and obj.display_topics==False and
    	obj.display_picture == True):

		template_path = "Forum/user-contribution-games-contributed.html"


	elif (request.user.is_authenticated and obj.display_topics==True and
		obj.display_picture == False):

		template_path = "Forum/user-contribution-do-not-display-picture.html"


	elif (request.user.is_authenticated and obj.display_topics==False and
		obj.display_picture == False):

		template_path = "Forum/user-contribution-gc-do-not-display-picture.html"


	else:

		template_path = "BASE.html"


	return render(request, template_path, context_dictionary)






def post_reply_in_reply(request, id):

	form = Reply_in_reply_Form(request.POST)

	reply_instance = Reply.objects.get(id=id)


	if request.method == 'POST':

		if form.is_valid():
			form.save()   
			obj = Reply_in_reply.objects.last()
			reply_instance.replies.add(obj)	
			
			print(request.user)
			obj.user = request.user
			print(obj.user)
			obj.save()

			form = Reply_in_reply_Form()
			return redirect('list_view')
		
	else:
		form = Reply_in_reply_Form()

	context_dictionary = {'form' : form,}
	                      

	if request.user.is_authenticated:
		template_path = "Forum/post-reply-in-reply.html"
	else:
		template_path = "BASE.html"

	return render(request, template_path, context_dictionary)





def update_reply_in_reply(request, id):

    obj=get_object_or_404(Reply_in_reply, id=id)

    form = Reply_in_reply_Form(request.POST or None, instance=obj)

    context_dictionary = {'form' : form, }

    if form.is_valid():
    	obj=form.save()
    	obj.save()
    	return HttpResponseRedirect("/list-posts")


    if request.user.is_authenticated and request.user==obj.user:

    	template_path = "Forum/update-post-reply-in-reply.html"
    else:
    	template_path = "BASE.html"


    return render(request, template_path, context_dictionary)





def user_account_view(request, id):

	obj = get_object_or_404(UserMember, id=id)

	if (request.user.is_authenticated and request.user.id == obj.id 
		and obj.simple_layout == True):

		template_path = "Forum/user-account-simple-layout.html"

	elif (request.user.is_authenticated and request.user.id == obj.id 
		and obj.simple_layout == False):

		template_path = "Forum/user-account.html"

	elif request.user.is_authenticated and request.user.id != obj.id:

		template_path = "Forum/you-are-not-authorized-to-view-this-page.html"

	else:

		template_path = "BASE.html"

	context = {'obj' : obj}

	return render(request, template_path, context)






# def create_user_profile(request):

# 	form =  Create_user_profile_Form(request.POST)



# 	if request.method == 'POST':

		

# 		if form.is_valid():
# 			#print(form.cleaned_data['question'])
# 			form.save()
# 			form = Create_user_profile_Form()
# 			return redirect('list_view')
# 	else:
# 			form = Create_user_profile_Form()

	
# 	context_dictionary = {
# 			 'form' : form,}

# 	if request.user.is_authenticated:
# 		template_path = "Forum/create-user-profile.html"
# 	else:
# 		template_path = "BASE.html"

# 	return render(request, template_path, context_dictionary)






def update_user_profile(request, id):

    obj=get_object_or_404(UserMember, id=id)

    form = Create_user_profile_Form(request.POST or None, request.FILES, instance=obj)

    context_dictionary = {'form' : form, }

    if form.is_valid():
    	obj=form.save()
    	obj.save()
    	return HttpResponseRedirect("/user/{id}".format(id=obj.id))

    print(request.user.id)
    print(obj.user.id)

    if request.user.is_authenticated and (request.user == obj.user or request.user.is_staff):

    	template_path = "Forum/create-user-profile.html"
    else:
    	template_path = "BASE.html"


    return render(request, template_path, context_dictionary)





def settings_view(request,id):


	obj=get_object_or_404(UserMember, id=id)

	form = SettingsForm(request.POST or None, instance=obj)

	context_dictionary = {'form' : form, }

	if form.is_valid():

		obj=form.save()
		obj.save()
		return HttpResponseRedirect("/settings/{id}".format(id=obj.id))

	if request.user.is_authenticated and (request.user == obj.user or request.user.is_staff):

		template_path = "Forum/settings-using-usermember.html"
	else:
		template_path = "BASE.html"

	return render(request, template_path, context_dictionary)






def list_user_members(request):

	qs = UserMember.objects.all()


	if request.user.is_authenticated:

		template_path = "Forum/usermembers.html"

	else:

		template_path = "BASE.html"

	context = {'qs' : qs}

	return render(request, template_path, context)





def send_email_message(request):

	form = SendMessageForm(request.POST)


	if request.method == 'POST':

		if form.is_valid():
			form.save()
			form = SendMessageForm()
			return redirect('list_view')
	else:
		form = SendMessageForm()

	

	context_dictionary = {'form' : form,}
	                      

	if request.user.is_authenticated:
		template_path = "Forum/send-mail-message.html"
	else:
		template_path = "BASE.html"

	return render(request, template_path, context_dictionary)





def display_mail_messages(request, id):

	qs1 =  UserMember.objects.get(id=id).messages.all()

	print("Qs count =", qs1.count())

	for item in qs1:
		print(item.to_user)
   
	

	context_dictionary = {
			     "qs1" : qs1,}
	

	if request.user.is_authenticated:

		template_path = "Forum/email-messages.html"

	else:

		template_path = "BASE.html"


	return render(request, template_path, context_dictionary)






def send_email_message_to_user(request,id):

	form = SendMessageForm(request.POST)

	usermember = UserMember.objects.get(id=id)


	if request.method == 'POST':

		if form.is_valid():
			form.save()
			obj = MailMessage.objects.last()
			usermember.messages.add(obj)
			form = SendMessageForm()
			return redirect('list_view')

		 
	else:
		form = SendMessageForm()

	context_dictionary = {'form' : form,}
	                      

	if request.user.is_authenticated  and usermember.receive_messages==True:

		template_path = "Forum/send-mail-message-to-user.html"

	elif request.user.is_authenticated and usermember.receive_messages == False:

		template_path =  "Forum/now-this-user-is-not-receiving-messages.html"
		
	else:
		template_path = "BASE.html"

	return render(request, template_path, context_dictionary)






def add_friend(request, id1, id2):


	try:

		usermember1 = UserMember.objects.get(id=id1)
		usermember2 = UserMember.objects.get(id=id2)

	except:

		raise Http404

	qs1 =  UserMember.objects.get(id=id2).usermember_topics.all()

	if request.method == 'POST':
		usermember1.friends.add(usermember2)
		return redirect('list_view')
    


	context_dictionary = {"usermember2" : usermember2,
			     "qs1" : qs1,}

	if (request.user.is_authenticated and request.user.id == usermember1.id 
		and usermember2.display_topics == True 
        and usermember2.become_friend==True):

		template_path = "Forum/user-contribution-add-friend.html"

	elif (request.user.is_authenticated and request.user.id == usermember1.id 
	and usermember2.display_topics == False
	and usermember2.become_friend == True):

		template_path = "Forum/user-contribution-games-contributed-add-friend.html"

	elif (request.user.is_authenticated and request.user.id == usermember1.id 
	and usermember2.become_friend == False):

		template_path = "Forum/now-this-user-is-not-accepting-friend-requests.html"


	elif (request.user.is_authenticated and request.user.id != usermember1.id):

		template_path = "Forum/unknown-request.html"  

	else:

		template_path = "BASE.html"


	return render(request, template_path, context_dictionary)





def view_friends_of_this_user(request, id):

	usermember = UserMember.objects.get(id=id)

	qs1 =  UserMember.objects.get(id=id).friends.all()

	

	context_dictionary = { "usermember" : usermember,
			     "qs1" : qs1,}
	

	if request.user.is_authenticated:

		template_path = "Forum/friends-list.html"

	else:

		template_path = "BASE.html"


	return render(request, template_path, context_dictionary)






def personalize_account(request, id):

	obj = UserMember.objects.get(id=id)

	form = AccountForm(request.POST or None,  request.FILES, instance=obj)


	if request.method == 'POST':

		if form.is_valid():
			obj=form.save()
			obj.save()
			return HttpResponseRedirect("/user-account/{id}".format(id=obj.id))


	else:
		form = AccountForm()

	
	context_dictionary = {'form' : form}

	if request.user.is_authenticated:
		template_path = "Forum/personalize-account.html"
	else:
		template_path = "BASE.html"

	return render(request, template_path, context_dictionary)






def usermember_delete_view(request, id):

	obj = get_object_or_404(UserMember, id=id)
	##POST request

	if request.method== 'POST':

		if 'yes' in request.POST:
			obj.delete()
			return redirect('welcome_to_game_apps_view')

		elif 'no' in request.POST:
			return HttpResponseRedirect("/user-account/{id}".format(id=obj.id))

	context = {'object' : obj}

	if request.user.is_authenticated:

		template_path = "Forum/delete-usermember-account.html"

	else:

		template_path = "BASE.html"

	return render(request, template_path, context)



 

