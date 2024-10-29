from django.contrib import admin
from django.contrib import admin
from .models import SiteSettings, About, Contact

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'email', 'phone')
    search_fields = ('site_title',)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('bio', 'profile_image', 'skills', 'cv_file')
    search_fields = ('bio', 'skills') 

    # Optional: If you want to display the links in a more structured way
    def get_links(self, obj):
        return obj.links if obj.links else "কোন লিঙ্ক নেই"
    get_links.short_description = 'কনটেস্ট লিঙ্কসমূহ'  # Column title in admin

    list_display += ('get_links',)  # Add the custom method to list_display

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message', 'created_at', 'status')  # নতুন ফিল্ডগুলো যুক্ত করা হলো
    search_fields = ('name', 'email', 'subject')

# Registering the models with the admin site
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
