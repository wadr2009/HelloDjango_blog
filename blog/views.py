import re

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from markdown.extensions.toc import TocExtension, slugify

from blog.models import Post
from django.shortcuts import render, get_object_or_404
import markdown


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list' : post_list
    })

def detail(request, id:int):
    post = get_object_or_404(Post, id=id)
    md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      TocExtension(slugify=slugify),
                                  ])
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', context={'post': post})