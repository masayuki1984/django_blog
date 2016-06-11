from django.shortcuts import *

def top(request):
    return render_to_response('top.html', locals(), context_instance=RequestContext(request))