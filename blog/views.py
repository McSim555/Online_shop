from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by('-created_at')

class ArticleCreateView(CreateView):
    model = Article
    fields = ['name', 'content', 'image', 'is_published']
    template_name = 'article_form.html'
    success_url = reverse_lazy('blog:article_list')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['name', 'content', 'image', 'is_published']
    template_name = 'article_form.html'
    success_url = reverse_lazy('blog:article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('blog:article_list')