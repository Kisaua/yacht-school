from django.contrib import admin

# Register your models here.

from .models import Contact, Portfolio


class ContactAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'user_email', )
    # pass


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('order', 'description', 'image', 'video', 'show')


admin.site.register(Contact, ContactAdmin)

admin.site.register(Portfolio, PortfolioAdmin)
