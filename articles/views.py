from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article


# Create your views here.
class ArticlesListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticlesDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticlesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.auther == self.request.user


class ArticlesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.auther == self.request.user


class ArticlesCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo',)
    template_name = 'article_new.html'

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
