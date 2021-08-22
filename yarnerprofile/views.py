from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import YarnerProfileForm

def yarnerprofile(request, username):
    user = get_object_or_404(User, username=username)
    yarns = user.yarns.all()

    for yarn in yarns:
        likes = yarn.likes.filter(created_by_id=request.user.id)

        if likes.count()>0:
            yarn.liked = True
        else:
            yarn.liked= False

    context= {
        'user': user,
        'yarns': yarns
    }

    return render(request, 'yarnerprofile/yarnerprofile.html', context)

@login_required
def edit_profile(request):
    if request.method== 'POST':
        form= YarnerProfileForm(request.POST, request.FILES, instance=request.user.yarnerprofile)

        if form.is_valid():
            form.save()

            return redirect('yarnerprofile', username=request.user.username)
    else:
        form= YarnerProfileForm(instance= request.user.yarnerprofile)

    context={
        'user': request.user,
        'form': form
    }

    return render(request, 'yarnerprofile/edit_profile.html', context)


@login_required
def follow_yarner(request, username):
    user= get_object_or_404(User, username=username)

    request.user.yarnerprofile.follows.add(user.yarnerprofile)

    return redirect('yarnerprofile', username=username)

@login_required
def unfollow_yarner(request, username):
    user= get_object_or_404(User, username=username)

    request.user.yarnerprofile.follows.remove(user.yarnerprofile)

    return redirect('yarnerprofile', username=username)

def followers(request, username):
    user= get_object_or_404(User, username=username)

    return render(request, 'yarnerprofile/followers.html', {'user': user})

def follows(request, username):
    user= get_object_or_404(User, username=username)

    return render(request, 'yarnerprofile/follows.html', {'user': user})
