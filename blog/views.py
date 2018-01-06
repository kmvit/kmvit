from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.

class BlogList(ListView):
    model = Blog
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tags_list'] = Tag.objects.all()
        return context

class BlogDetail(DetailView):
    model = Blog
    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tags_list'] = Tag.objects.all()
        return context

class CategoryDetail(DetailView):
    model = Category
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tags_list'] = Tag.objects.all()
        context['blog_list'] = Blog.objects.filter(category__slug=self.kwargs['slug'])
        return context

class TagsDetail(DetailView):
    model = Tag
    def get_context_data(self, **kwargs):
        context = super(TagsDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tags_list'] = Tag.objects.all()
        context['blog_list'] = Blog.objects.filter(tags__slug=self.kwargs['slug'])
        return context