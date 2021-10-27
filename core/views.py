from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Blog
from django.db.models import Q

# Create your views here.
def searchView(request):
    if request.method == 'GET':
        if request.GET['search']:
            query = request.GET.get('search')
            try:
                blog_lookup = Q(title__icontains = query)
                blog_filter = Blog.objects.filter(blog_lookup)
                context = {
                    'blog_filter' : blog_filter
                }
                return render(request, "home.html", context)
            except:
                pass
        else:
            return render(request, "home.html")
    else:
        return render(request, "home.html")

class ClientHomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bloglist'] = Blog.objects.all().order_by('-id')
        return context