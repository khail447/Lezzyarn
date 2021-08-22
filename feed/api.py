import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Like, Yarn
@login_required
def api_add_yarn(request):
    data= json.loads(request.body)
    body= data['body']

    yarn = Yarn.objects.create(body=body, created_by=request.user)

    return JsonResponse({'success': True})

@login_required
def api_add_like(request):
    data = json.loads(request.body)
    yarn_id = data['yarn_id']

    if not Like.objects.filter(yarn_id=yarn_id).filter(created_by=request.user).exists():
        like = Like.objects.create(yarn_id=yarn_id, created_by=request.user)

    return JsonResponse({'success': True})