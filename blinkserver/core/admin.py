from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_admin_bootstrapped.admin.models import SortableInline
from blinkserver.core.models import BlinkStatus ,Hook
from django.forms import ModelForm
from django.forms.widgets import HiddenInput ,TextInput
from django import forms

class BlinkStatusInlineForm(ModelForm):

    class Meta:
        model = BlinkStatus
        widgets = {
            'position': HiddenInput(),
        }
        fields = ('duration','fading_time','red','green','blue','position')


class BlinkStatusInline(admin.StackedInline, SortableInline):
    model = BlinkStatus
    extra = 0
    max_num=12
    form = BlinkStatusInlineForm


class HookAdmin(admin.ModelAdmin):
    fields = ('name','private',)
    list_display=('name','link_to_hook')
    ordering = ('name',)
    search_fields = ['name']
    inlines = [
        BlinkStatusInline,
    ]
    class Media:
        css = {
            "add": ("colorpicker/css/colorpicker.css",),
            "change": ("colorpicker/css/colorpicker.css",)
        }
        js = ("colorpicker/js/bootstrap-colorpicker.js",)

    def queryset(self, request):
        qs = super(HookAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

    def link_to_hook(self,obj):
        return "<a href='%s' ><li class='icon-tag'></li></a>" % reverse('public_hook',  args=[obj.name])

    link_to_hook.allow_tags = True



admin.site.register(Hook, HookAdmin)
