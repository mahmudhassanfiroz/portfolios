from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonial_list'),
    
    path('services/', views.ServiceListView.as_view(), name='service_list'),

    path('services/<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),  # Detail view URL

]
