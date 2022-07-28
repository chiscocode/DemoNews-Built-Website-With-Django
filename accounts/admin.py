from django.contrib import admin

# Register your models here.
from .models import *
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','date_added')
    list_filter = ("title",)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ['title',]

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','status','date_added')
    list_filter = ("title",)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ['title',]

class FeaturedPostAdmin(admin.ModelAdmin):
    list_display = ('title','category','status','date_added')
    list_filter = ("title",)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ['title',]

class MainPostAdmin(admin.ModelAdmin):
    list_display = ('title','category','status','date_added')
    list_filter = ("title",)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ['title',]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body')
    list_filter = ("name",)
    search_fields = ['name', 'body']

class FeaturedCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body')
    list_filter = ("name",)
    search_fields = ['name', 'body']

class MainCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body')
    list_filter = ("name",)
    search_fields = ['name', 'body']

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject')
    list_filter = ("email",)
    search_fields = ['email', 'subject']

admin.site.register(Contact,ContactAdmin)
admin.site.register(AdvertisementOne)
admin.site.register(AdvertisementThree)
admin.site.register(Newsletter)
admin.site.register(FeaturedComment,FeaturedCommentAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(MainComment,MainCommentAdmin)
admin.site.register(FeaturedPost,FeaturedPostAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(MainPost,MainPostAdmin)
admin.site.register(Category,CategoryAdmin)