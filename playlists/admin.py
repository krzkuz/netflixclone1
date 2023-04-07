from django.contrib import admin

from .models import (
    Playlist, 
    PlayListItem, 
    TVShowProxy, 
    TVShowSeasonProxy,
    MovieProxy
    )


class MovieProxyAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'state', 'video', 'category', 'slug']
    list_display = ['title']
    
    class Meta:
        model = MovieProxy

    def get_queryset(self, request):
        return MovieProxy.objects.all()
    

admin.site.register(MovieProxy, MovieProxyAdmin)


class PlaylistItemInLine(admin.TabularInline):
    model = PlayListItem


class TVShowSeasonProxyAdmin(admin.ModelAdmin):
    inlines = [PlaylistItemInLine]
    list_display = ['title', 'parent']
    class Meta:
        model = Playlist

    def get_queryset(self, request):
        return TVShowSeasonProxy.objects.all()


admin.site.register(TVShowSeasonProxy, TVShowSeasonProxyAdmin)


class TVShowSeasonProxyInLine(admin.TabularInline):
    model = TVShowSeasonProxy
    extra = 0
    fields = ['order', 'title', 'state']


class TVShowProxyAdmin(admin.ModelAdmin):
    inlines = [TVShowSeasonProxyInLine]
    fields = ['title', 'description', 'state', 'video', 'category', 'slug']
    list_display = ['title']
    class Meta:
        model = TVShowProxy

    def get_queryset(self, request):
        return TVShowProxy.objects.all()


admin.site.register(TVShowProxy, TVShowProxyAdmin)


class PlaylistItemInLine(admin.TabularInline):
    model = PlayListItem


class PlayListAdmin(admin.ModelAdmin):
    inlines = [PlaylistItemInLine]
    class Meta:
        model = Playlist

    def get_queryset(self, request):
        return Playlist.objects.filter(type='PLY')

admin.site.register(Playlist, PlayListAdmin)
