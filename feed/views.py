from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Yarn
# Create your views here.
@login_required
def feed(request):
    userids = [request.user.id]

    for yarner in request.user.yarnerprofile.follows.all():
        userids.append(yarner.user.id)

    yarns= Yarn.objects.filter(created_by_id__in=userids)

    for yarn in yarns:
        likes = yarn.likes.filter(created_by_id=request.user.id)

        if likes.count()>0:
            yarn.liked = True
        else:
            yarn.liked= False

    return render(request, 'feed/feed.html', {'yarns': yarns})

@login_required
def search(request):
    query=request.GET.get('query', '')

    if len(query)> 0:
        yarners= User.objects.filter(username__icontains=query)
    else:
        yarners=[]

    context={
        'query': query,
        'yarners': yarners
    }

    return render(request,'feed/search.html',context )

