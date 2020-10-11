from django.contrib import admin

# Register your models here.




from .models import (Discussion, Email, Reply, UserMember, Reply_in_reply, 
					MailMessageReply, MailMessage)







admin.site.register(Discussion)
admin.site.register(Email)
admin.site.register(Reply)
admin.site.register(UserMember)
admin.site.register(Reply_in_reply)
admin.site.register(MailMessageReply)
admin.site.register(MailMessage)
