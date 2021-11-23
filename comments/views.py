from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Post

# Create your views here.
from comments.forms import CommentForm


@require_POST
def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(post)