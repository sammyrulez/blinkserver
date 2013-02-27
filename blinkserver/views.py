# Create your views here.
from blinkserver.core.models import BlinkStatus ,Hook

def hook(request,hook_name):
    req_hook = Hook.objects.get(name__exact = hook_name)