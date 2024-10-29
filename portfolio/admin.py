from django.contrib import admin
from .models import Project, Service, Testimonial

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at', 'is_featured')
    list_filter = ('is_featured', 'technology')
    search_fields = ('title', 'description', 'technology')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    list_editable = ('is_featured',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company', 'rating', 'is_active')
    list_filter = ('is_active', 'rating')
    search_fields = ('name', 'company', 'content')
    list_editable = ('is_active', 'rating')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'slug')  # Display title, icon, and slug in the list
    search_fields = ('title',)  # Search by title

    def icon(self, obj):
        return f'<i class="{obj.icon}"></i>'  # Create icon from class name
    icon.allow_tags = True  # Allow HTML tags in the admin interface

