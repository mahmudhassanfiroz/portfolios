# protfolio/core/views.py

from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages

from .forms import ContactForm
from portfolio.models import Project, Service 
from .models import SiteSettings, About, Contact
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['featured_projects'] = Project.objects.filter(is_featured=True)  # Fetch featured projects
        context['services'] = Service.objects.all()  # Fetch all services
        context['about'] = About.objects.first()  # Fetch the first About instance
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = About.objects.first()
        about.skills = about.skills.strip() if about.skills else ''  # Trim whitespace
        context['about'] = about
        
        return context

# class ContactView(TemplateView):
#     template_name = 'core/contact.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = ContactForm()
#         return context

#     def post(self, request, *args, **kwargs):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your message has been sent successfully!')
#             return redirect('core:home')
#         else:
#             messages.error(request, 'Please provide valid information.')
#             return self.get(request, *args, **kwargs)

class ContactView(FormView):  # Changed from View to FormView
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:home')  # Redirect after successful submission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()  # Add contact information
        return context

    def form_valid(self, form):
        form.save()  # Save form data
        messages.success(self.request, 'Your message has been sent successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please provide valid information.')
        return super().form_invalid(form)

