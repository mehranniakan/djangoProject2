import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from blog.models import Post


def home_blog(request):
    current_date = timezone.now().date()
    post = Post.objects.filter(Publish_date__lte=current_date, Status=True)
    context = {'Posts': post}
    return render(request, "blog/blog-home.html", context)


def single_blog(request, pid):
    current_date = timezone.now().date()
    base_query = get_object_or_404(Post, pk=pid, Publish_date__lte=current_date, Status=True)

    count = base_query.Counted_Views
    count = count + 1

    query = Post.objects.filter(pk=pid).update(Counted_Views=count)

    base_query = get_object_or_404(Post, pk=pid, Publish_date__lte=current_date, Status=True)

    get_items = Post.objects.filter(Publish_date__lte=current_date, Status=True)
    get_items = list(get_items)

    index = -1
    next_item = "Null"
    prev_item = "Null"

    for x in get_items:
        index += 1
        if pid == x.id:
            try:
                next_item = get_items[index + 1]
            except:
                next_item = 'Null'

            try:
                if index == 0:
                    pass
                else:
                    prev_item = get_items[index - 1]
            except:
                next_item = 'Null'

        else:
            pass
    context = {'Post': base_query, 'next_item': next_item, 'prev_item': prev_item}
    return render(request, "blog/Blog-single.html", context)


def test(request, pid):
    now = timezone.now().date()
    context = {'Time': now}
    return render(request, "blog/test.html", context)
