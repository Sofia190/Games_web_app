from django.db import models

# Create your models here.




from django.utils import timezone



class GameApp1stQuerySet(models.query.QuerySet):

	# def active(self):
	# 	return self.filter(active=True)

	def GameApp1st_name_items(self, value):
		return self.filter(name__icontains='game')




class GameApp1stModelManager(models.Manager):

	def get_queryset(self):
		    return GameApp1stQuerySet(self.model, using=self._db)


	def get_time_frame(self, date1, date2):
    		qs=self.get_queryset()
    		qs_time_1 = qs.filter(release__gte=date1)
    		qs_time_2=qs_time_1.filter(release__lt=date2) # Q lookups

		 

    		#qs_time_2=qs.filter(publish_date__lte=date2)
		    #final_qs = (qs_time_1 | qs_time_2).distinct() #removes duplicates from the queryset


    		return qs_time_2







class GameApp_1st(models.Model):


    name = models.CharField(max_length=270)
    description = models.TextField(default='Game app description')
    release = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())

    objects = GameApp1stModelManager()     #or objectsmodelmanager























