from django.contrib import admin
from .models import Post
from .models import Post2


class PostAdmin(admin.ModelAdmin):
	list_display=('title','author','created_date','published_date')
	search_fields =('title',)

# Register your models here.
admin.site.register(Post,PostAdmin)



class PostAdmin2(admin.ModelAdmin):
	list_display=('country_name','author','created_date','published_date')
	search_fields =('country_name',)

# Register your models here.
admin.site.register(Post2,PostAdmin2)
