from django.contrib import admin

from .models import Playlist, PlayListItem, TVShowProxy


class TVShowProxyInLine(admin.TabularInline):
    model = TVShowProxy
    extra = 0
    fields = ['order', 'title', 'state']

class TVShowProxyAdmin(admin.ModelAdmin):
    inlines = [TVShowProxyInLine]
    class Meta:
        model = TVShowProxy

    def get_queryset(self, request):
        return TVShowProxy.objects.all()
    

class PlaylistItemInLine(admin.TabularInline):
    model = PlayListItem


class PlayListAdmin(admin.ModelAdmin):
    inlines = [PlaylistItemInLine]
    class Meta:
        model = Playlist

admin.site.register(Playlist, PlayListAdmin)
admin.site.register(TVShowProxy, TVShowProxyAdmin)