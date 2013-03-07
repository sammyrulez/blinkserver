# Create your views here.
from blinkserver.core.models import BlinkStatus ,Hook
from blinkserver import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from functools import wraps
from django.shortcuts import redirect

def http_basic_auth(func):
    @wraps(func)
    def _decorator(request, *args, **kwargs):
        from django.contrib.auth import authenticate, login
        if request.META.has_key('HTTP_AUTHORIZATION'):
            authmeth, auth = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
            if authmeth.lower() == 'basic':
                auth = auth.strip().decode('base64')
                username, password = auth.split(':', 1)
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
        return func(request, *args, **kwargs)
    return _decorator

def hook(request,hook_name):
    req_hook = Hook.objects.get(name__exact = hook_name)
    if req_hook.private:
        return HttpResponse('Unauthorized', status=401)
    #TODO this should be queued
    blink = settings.BLINK_MANAGER
    try:
        blink.stop()
    except:
        pass

    pattern = [(0.25, (0, 0, 0))]

    for step in req_hook.blinkstatus_set.all():
        transition_time = 0.25
        if step.fading_time:
           transition_time = step.fading_time
        pattern.append((transition_time,(step.red, step.green, step.blue)))
        pattern.append((step.duration,(step.red, step.green, step.blue)))

    blink.set_pattern(pattern)
    blink.play()

    return HttpResponse('Ok', status=200)

@login_required
@staff_member_required
def stop_blink(request):
    blink = settings.BLINK_MANAGER
    try:
        blink.stop()
        blink.set_rgb(0,0,0)
    except:
        pass
    return redirect('admin:index')

@http_basic_auth
def private_hook(request,hook_name):
    #todo
    return HttpResponse('Ok', status=200)

