from django.contrib import admin

from .models import Project, ChatProject, Message
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display        = ('title','customer_name','status')
    list_display_links  = ('title',)
    list_filter         = ('created','modified','status')


@admin.register(ChatProject)
class ChatProjectAdmin(admin.ModelAdmin):

    list_display        = ('name','created')
    list_display_links  = ('name',)
    search_fields       = ('name',)
    list_filter         = ('created',)

@admin.register(Message)
class ChatProjectAdmin(admin.ModelAdmin):

    list_display        = ('timestamp','author','sala')
    list_display_links  = ('timestamp',)
    list_filter         = ('sala',)