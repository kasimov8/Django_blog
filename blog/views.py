from dataclasses import dataclass
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from blog.forms import FormsBlog
from blog.models import Blog

def home(request):
    context = {
        'blogs': Blog.objects.filter(is_active=True)
    }

    return render(request, template_name='blog/home.html', context=context)

def inactive(request):
    context = {
        'blogs': Blog.objects.filter(is_active=False)
    }

    return render(request, template_name='blog/inactive.html', context=context)


def about(request):
    context = {
    }
    return render(request, template_name='blog/about.html', context=context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        "blog": blog
    }
    return render(request, template_name='blog/detail.html', context=context)

def update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = FormsBlog(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            messages.success(request, message=f"{blog.title} o'zgartirildi!")
            return redirect('home')
    else:
        form = FormsBlog(instance=blog)

    context = {
        "form": form,
        "blog": blog
    }
    return render(request, 'blog/update.html', context=context)

def delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = FormsBlog(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            blog = form.save()
            messages.success(request, message=f"{blog.title} yaratildi!")
            return redirect('home')
    else:
        messages.warning(request, message=f"Hozirda biz test rejimida ishlayapmiz!")
        form = FormsBlog()


    context = {
        "form" : form
    }
    return render(request, 'blog/create_blog.html', context=context)