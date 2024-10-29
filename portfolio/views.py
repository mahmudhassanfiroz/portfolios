from django.views.generic import ListView, DetailView
from .models import Project, Service, Testimonial

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolios/project_list.html'
    context_object_name = 'projects'


class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'portfolios/testimonial_list.html'
    context_object_name = 'testimonials'

    def get_queryset(self):
        return Testimonial.objects.filter(is_active=True)


class ServiceListView(ListView):
    model = Service
    template_name = 'protfolios/service_list.html' 
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'protfolios/service_detail.html' 
    context_object_name = 'service'

