# Create your views here.
from blinkserver.core.models import BlinkStatus ,Hook
from blinkserver import settings
import threading

from functools import wraps

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
    for step in req_hook.blinkstatus_set.all():
        if step.fading_time:
            blink.fade_to_rgb(step.fading_time / 1000 , step.red, step.green, step.blue):
        else:
            blink.set_rgb(step.red, step.green, step.blue)
        t = Timer(step.duration, hello)

def _output_step(step):
    pass
