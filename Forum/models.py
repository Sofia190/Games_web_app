from django.conf import settings


from django.db import models

# Create your models here.

from django.utils import timezone

from GameApps.models_1st import GameApp_1st



User = settings.AUTH_USER_MODEL    #auth.USER


class Email(models.Model):
	email_addr = models.CharField(max_length=35)



class Reply_in_reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)  
    reply_content = models.TextField(default='Post your comment here')
    replied_by = models.CharField(max_length=35, default='user member')
    post_date=models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    contact_author=models.BooleanField(default=False)
    contact_details = models.ForeignKey(Email, on_delete=models.CASCADE, default=True)






class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)  
    replies = models.ManyToManyField(Reply_in_reply)
    reply_content = models.TextField(default='Post your comment here')
    replied_by = models.CharField(max_length=35, default='user member')
    post_date=models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    contact_author=models.BooleanField(default=False)
    contact_details = models.ForeignKey(Email, on_delete=models.CASCADE, default=True)



class Discussion(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)  
    title =models.CharField(max_length=270)
    content = models.TextField()
    started_by = models.CharField(max_length=35)
    posted=models.BooleanField(default=False)
    post_date=models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    d_replies=models.ManyToManyField(Reply, related_name='r_query')





class MailMessageReply(models.Model):

    title = models.CharField(max_length=150, default='message')
    message =  models.TextField(default='Write your message here')
    from_user = models.CharField(max_length=70, default='user member')
    to_user = models.ManyToManyField(User, default=True)  
    sent = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())





class MailMessage(models.Model):

     
    title = models.CharField(max_length=150, default='message')
    message =  models.TextField(default='Write your message here')
    from_user = models.CharField(max_length=70, default='user member')
    to_user = models.ManyToManyField(User, default=True)
    sent = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    replies = models.ManyToManyField(MailMessageReply, default=True)









class UserMember(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)  
    usermember = models.ForeignKey(Reply, on_delete=models.CASCADE, default=True)
    usermember_topics=models.ManyToManyField(Discussion, related_name='d_query')
    games=models.ManyToManyField(GameApp_1st, related_name='g_query')
    name = models.CharField(max_length=35, default='user member')

    image = models.ImageField(upload_to='image/', blank=True, null=True, default=None)
    description = models.TextField(default='Write about you here')
    join_date=models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    contact_author=models.BooleanField(default=False)
    contact_details = models.ForeignKey(Email, on_delete=models.CASCADE, default=True)
    social_profile_1 = models.TextField(default='')
    social_profile_2 = models.TextField(default='')


    work_experience = models.TextField(default='Write about your work here')
    work_start_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    work_end_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    company_name =  models.CharField(max_length=100, default='company name')
    attribute =  models.CharField(max_length=50, default='attribute')


    work_experience_1= models.TextField(default='Write about your work here')
    work_1_start_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    work_1_end_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    company_1_name =  models.CharField(max_length=100, default='company name')
    attribute_1=  models.CharField(max_length=50, default='attribute')



    work_experience_2 = models.TextField(default='Write about your work here')
    work_2_start_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    work_2_end_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    company_2_name =  models.CharField(max_length=100, default='company name')
    attribute_2 =  models.CharField(max_length=50, default='attribute')
 


    education = models.TextField(default='Write about your education here')
    education_start_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    education_domain = models.CharField(max_length=70, default='certification domain')
    institution = models.CharField(max_length=200, default='institution')



    education_1 = models.TextField(default='Write about your education here')
    education_1_start_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    education_1_domain = models.CharField(max_length=70, default='certification domain')
    institution_1 = models.CharField(max_length=200, default='institution')


    education_2 = models.TextField(default='Write about your education here')
    education_2_start_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    education_2_domain = models.CharField(max_length=70, default='certification domain')
    institution_2 = models.CharField(max_length=200, default='institution')


    

    ref_from_person = models.CharField(max_length=50, default='employer')
    ref_description = models.TextField(default='Write about your reference here')
    ref_from_person_pos = models.CharField(max_length=50, default='hiring person')
    ref_from_company = models.CharField(max_length=100, default='company name')



    ref_1_from_person = models.CharField(max_length=50, default='employer')
    ref_1_description = models.TextField(default='Write about your reference here')
    ref_1_from_person_pos = models.CharField(max_length=50, default='hiring person')
    ref_1_from_company = models.CharField(max_length=100, default='company name')



    ref_2_from_person = models.CharField(max_length=50, default='employer')
    ref_2_description = models.TextField(default='Write about your reference here')
    ref_2_from_person_pos = models.CharField(max_length=50, default='hiring person')
    ref_2_from_company = models.CharField(max_length=100, default='company name')



    portofolio_project_name = models.CharField(max_length=100, default='project name')
    portofolio_project_domain = models.CharField(max_length=70, default=' domain')


    portofolio_project_1_name = models.CharField(max_length=100, default='project name')
    portofolio_project_1_domain = models.CharField(max_length=70, default=' domain')

    portofolio_project_2_name = models.CharField(max_length=100, default='project name')
    portofolio_project_2_domain = models.CharField(max_length=70, default=' domain')

    portofolio_project_3_name = models.CharField(max_length=100, default='project name')
    portofolio_project_3_domain = models.CharField(max_length=70, default=' domain')

    portofolio_project_4_name = models.CharField(max_length=100, default='project name')
    portofolio_project_4_domain = models.CharField(max_length=70, default=' domain')

    portofolio_project_5_name = models.CharField(max_length=100, default='project name')
    portofolio_project_5_domain = models.CharField(max_length=70, default=' domain')


    skill_1 = models.CharField(max_length=70, default='extra skill')
    skill_2 = models.CharField(max_length=70, default='extra skill')
    skill_1_percentage = models.IntegerField(default=70)
    skill_2_percentage = models.IntegerField(default=70)
    phrase_1 = models.CharField(max_length=120, default="quote")
    phrase_2 = models.CharField(max_length=120, default="quote")
    years_of_experience = models.IntegerField(default=0)
    awards_won = models.IntegerField(default=0)



    private=models.BooleanField(default=False)

    display_topics = models.BooleanField(default=True)

    receive_messages = models.BooleanField(default=True)

    display_picture = models.BooleanField(default=True)

    simple_layout = models.BooleanField(default=True)

    become_friend = models.BooleanField(default=True)


    messages = models.ManyToManyField(MailMessage, default=True)

    
    friends = models.ManyToManyField("self", default=True, blank=True)

    account_image = models.ImageField(upload_to='image/', blank=True, null=True)

    favourite_games = models.TextField(default='Write about your favourite games here')



























	






