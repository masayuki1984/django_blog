from django.shortcuts import *
from posts.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def top(request):
    all_posts = Post.objects.all()

    # Paginator
    paginator = Paginator(all_posts, 5)
    page = request.GET.get('page')
    try:
        all_posts = paginator.page(page)
    except PageNotAnInteger:
        all_posts = paginator.page(1)
    except EmptyPage:
        all_posts = paginator.page(paginator.num_pages)
    return render_to_response('top.html', {"all_posts":all_posts}, context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))