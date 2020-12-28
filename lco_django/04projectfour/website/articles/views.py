from django.views.generic import ListView , DetailView

# Create your views here.
from .models import Articles

class ArticleListView(ListView):
    model = Articles
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name = 'batman'
