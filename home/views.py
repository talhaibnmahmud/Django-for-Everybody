from django.views.generic import TemplateView


# Create your views here.
class MainView(TemplateView):
    template_name = 'home/main.html'
