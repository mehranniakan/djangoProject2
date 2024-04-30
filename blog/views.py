import datetime

from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


# Create your views here.


def home_blog(request, catname=None, auth_name=None):
    if catname is None and auth_name is None:
        current_date = timezone.now().date()
        post = Post.objects.filter(Publish_date__lte=current_date, Status=True).order_by('Publish_date')
        pages = Paginator(post, 3)
        page_number = request.GET.get('Page')
        try:
            page_obj = pages.page(page_number)

        except InvalidPage:
            pages = Paginator(post, 3)
            page_obj = pages.get_page(1)

        context = {'Posts': page_obj}
        return render(request, "blog/blog-home.html", context)

    elif catname is not None and auth_name is None:
        now = timezone.now().date()
        posts = Post.objects.filter(Status=True, Publish_date__lte=now, Category__Name=catname)
        context = {'Posts': posts}
        return render(request, "blog/blog-home.html", context)

    elif catname is None and auth_name is not None:
        now = timezone.now().date()
        posts = Post.objects.filter(Status=True, Publish_date__lte=now, Author__username=auth_name)
        print(auth_name)
        context = {'Posts': posts}
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


def search_blog(request):
    context = {}
    if request.method == "GET":
        current_date = timezone.now().date()
        val = request.GET.get('SV')
        print(val)
        posts = Post.objects.filter(Status=True, Publish_date__lte=current_date)
        posts = posts.filter(Q(Content__contains=val) | Q(Title__contains=val))
        context = {'Posts': posts}
    return render(request, "blog/blog-home.html", context)


def test(request, pid):
    now = timezone.now().date()
    context = {'Time': now}
    return render(request, "blog/test.html", context)
