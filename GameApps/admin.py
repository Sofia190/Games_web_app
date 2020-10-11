from django.contrib import admin

# Register your models here.


from .models import GameApp, ProducerCompany, Rule

from .models_1st import GameApp_1st


admin.site.register(GameApp)
admin.site.register(ProducerCompany)
admin.site.register(GameApp_1st)
admin.site.register(Rule)



















