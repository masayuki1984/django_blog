from django.shortcuts import *
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def detail(request, id):
    post = Post.objects.get(id=id)
    print 'POST:%s' %post.id

    try:
        new_post = Post.objects.get(id=post.id+1)
        print 'new_post_id: %s' %new_post.id
    except:
        pass

    try:
        old_post = Post.objects.get(id=post.id-1)
        print 'old_post_id: %s' %old_post.id
    except:
        pass

    return render_to_response('posts/detail.html', locals(), context_instance=RequestContext(request))

@login_required
def add_entry(request):
    entry_form = PostForm

    # check a request method
    if request.method =='POST':
        entry = PostForm(request.POST or None)
        # check entry data. It is valid or not
        if entry.is_valid():
            new_entry = entry.save(commit=False)
            new_entry.save()
            return HttpResponseRedirect('/')

    return render_to_response('posts/add_entry.html', {"entry_form":entry_form}, context_instance=RequestContext(request))

@login_required
def edit_entry(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        new_post = PostForm(request.POST or None, instance=post)

        if new_post.is_valid():
            newest_post = new_post.save(commit=False)
            newest_post.save()

            return HttpResponseRedirect('/posts/detail/%s/' %post.id)

    return render_to_response('posts/edit_entry.html', locals(), context_instance=RequestContext(request))

@login_required
def delete_entry(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        # We will delete this post object
        post.delete()

        return HttpResponseRedirect('/')