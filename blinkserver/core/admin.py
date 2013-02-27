from django.contrib import admin
from django.contrib.auth.models import User
from blinkserver.core.models import BlinkStatus ,Hook

class BlinkStatusInline(admin.TabularInline):
    model = BlinkStatus

class HookAdmin(admin.ModelAdmin):
    fields = ('name','private',)
    list_fileds=('name',)
    ordering = ('name',)
    search_fields = ['name']
    inlines = [
        BlinkStatusInline,
    ]

    def queryset(self, request):
        qs = super(HookAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


admin.site.register(Hook, HookAdmin)