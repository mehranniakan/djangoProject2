import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


def home_blog(request):
    current_date = datetime.date.today()
    post = Post.objects.filter(Publish_date__lte=current_date, Status=True)
    context = {'Posts': post}
    return render(request, "blog/blog-home.html", context)


def single_blog(request, pid):
    base_query = get_object_or_404(Post, pk=pid, Status=True)
    count = base_query.Counted_Views
    count = count + 1
    query = Post.objects.filter(pk=pid).update(Counted_Views=count)
    get_items = Post.objects.all()

    index = -1
    next_id = pid
    prev_id = pid

    try:
        for x in get_items:
            index += 1
            if pid == x.pk:
                next_id = get_items[index + 1].id
                prev_id = get_items[index - 1].id
            else:
                pass
    except:
        print('Nothing to Show')

    context = {'Post': base_query, 'count': count, 'next_id': next_id, 'prev_id': prev_id}
    return render(request, "blog/Blog-single.html", context)


def test(request, age):
    context = {'Posts': age}
    return render(request, "blog/test.html", context)
