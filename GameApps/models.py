from django.db import models

# Create your models here.


from Forum.models import UserMember

from Forum.models import MailMessage

from django.utils import timezone



class GameApp(models.Model):


    authors = models.ManyToManyField(UserMember, related_name='a_query')
    name = models.CharField(max_length=270)
    description = models.TextField(default='Game app description')
    release = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
    rating = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)






class ProducerCompany(models.Model):

	afiliated = models.ManyToManyField(UserMember, related_name='author_query')
	name = models.CharField(max_length=270)
	activity = models.TextField(default='Company activity')
	started = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	messages = models.ManyToManyField(MailMessage, default=True)





class RuleQuerySet(models.query.QuerySet):


	def Rule_name_items(self, value):
		return self.filter(content__icontains='rule')





class RuleModelManager(models.Manager):


	def get_queryset(self):
		    return RuleQuerySet(self.model, using=self._db)



	def get_time_frame_active(self):

		qs_active=self.get_queryset()

		count_1st = 0

		for item in qs_active:

			if ((item.start_date == item.end_date  or  item.end_date > item.today) or 
    			(item.start_date < item.today and  item.end_date > item.today)):

				count_1st+=1

		return count_1st




	def get_time_frame_inactive(self):

		qs_inactive=self.get_queryset()

		count_2nd = 0

		for item in qs_inactive:

			if (item.end_date < item.today):

				count_2nd+=1

		return count_2nd




	def get_time_frame(self, date1, date2):
    		qs=self.get_queryset()
    		qs_time_1 = qs.filter(start_date__gte=date1)
    		qs_time_2=qs_time_1.filter(start_date__lt=date2) 


    		return qs_time_2





class Rule(models.Model):

	content =  models.TextField(default='the content of the rule')
	start_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	end_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	today = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())

	objects = RuleModelManager() 





