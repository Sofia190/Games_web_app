
from django.forms import ModelForm

from . models import (Discussion, Reply, Reply_in_reply, UserMember, 
						 MailMessage)




# from django import forms 
  



class MessageForm(ModelForm):

	class Meta:

		model = Discussion

		fields = ['title', 'content']


class ReplyForm(ModelForm):

	class Meta:

		model = Reply

		fields = [ 'reply_content']


class PostForm(ModelForm):

	class Meta:

		model = Discussion

		fields = ['title', 'content']



class Reply_in_reply_Form(ModelForm):

	class Meta:

		model = Reply_in_reply

		fields = [ 'reply_content']







class Create_user_profile_Form(ModelForm):

	class Meta:

		model = UserMember

		fields = ['name', 'image', 'description', "join_date", "contact_details", "social_profile_1",

		         'work_experience', 'work_start_date', 'work_end_date', 'company_name', 'attribute',

	         'work_experience_1', 'work_1_start_date', 'work_1_end_date', 'company_1_name', 'attribute_1',

	         'work_experience_2', 'work_2_start_date', 'work_2_end_date', 'company_2_name', 'attribute_2',
 
                 'education', 'education_start_date', 'education_domain', 'institution', 

                 'education_1', 'education_1_start_date', 'education_1_domain', 'institution_1', 

                 'education_2', 'education_2_start_date', 'education_2_domain', 'institution_2',

                 'ref_from_person', 'ref_description', 'ref_from_person_pos', 'ref_from_company',

                 'ref_1_from_person', 'ref_1_description', 'ref_1_from_person_pos', 'ref_1_from_company',

                 'ref_2_from_person', 'ref_2_description', 'ref_2_from_person_pos', 'ref_2_from_company',

                 'portofolio_project_name', 'portofolio_project_domain',

                  'portofolio_project_1_name', 'portofolio_project_1_domain',

                  'portofolio_project_2_name', 'portofolio_project_2_domain',

                   'portofolio_project_3_name', 'portofolio_project_3_domain', 

                  'portofolio_project_4_name', 'portofolio_project_4_domain', 

                   'portofolio_project_5_name', 'portofolio_project_5_domain', 

                   'skill_1', 'skill_1_percentage', 'phrase_1',  
                   'skill_2','skill_2_percentage', 'phrase_2', 'years_of_experience', 'awards_won' ]



 

class SettingsForm(ModelForm):

	class Meta: 

		model = UserMember

		fields = ['private', 'display_topics', 'receive_messages', 'display_picture', 'simple_layout', 'become_friend']





class SendMessageForm(ModelForm):

	class Meta:

		model  = MailMessage

		fields = ['from_user', 'to_user', 'title', 'message']





class AccountForm(ModelForm):

	class Meta:

		model = UserMember

		fields = ['account_image', 'favourite_games']




