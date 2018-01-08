from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
        blog_list = Blog.objects.filter(category__slug=self.kwargs['slug'])
        page = self.request.GET.get('page', 1)
        paginator = Paginator(blog_list, 10)
        try:
            context['blog_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['blog_list'] = paginator.page(1)
        except EmptyPage:
            context['blog_list'] = paginator.page(paginator.num_pages)
        return context

class TagsDetail(DetailView):
    model = Tag
    def get_context_data(self, **kwargs):
        context = super(TagsDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tags_list'] = Tag.objects.all()
        context['blog_list'] = Blog.objects.filter(tags__slug=self.kwargs['slug'])
        return context