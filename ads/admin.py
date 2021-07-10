from django.contrib import admin
from ads.models import Ad, Comment, Fav


class AdAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register your models here.
admin.site.register(Ad, AdAdmin)
admin.site.register(Comment)
admin.site.register(Fav)
