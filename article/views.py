from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic

from .models import Article

# Create your views here.

def home(request):
	return render(request, "article/home.html")

def about(request):
	return render(request, "article/about.html")

class IndexView(generic.ListView):
	template_name = 'article/index.html'
	context_object_name = 'article_list'

	def get_queryset(self):
		return Article.objects.all().order_by('-pub_date')

class DetailView(generic.DetailView):
	model = Article
	template_name = 'article/detail.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now
		return context