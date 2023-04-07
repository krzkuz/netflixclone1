from django.contrib import admin

from .models import VideoPublishedProxy, VideoAllProxy


class VideoAllProxyAdmin(admin.ModelAdmin):
    list_display = [
        'title', 
        'id', 
        'video_id', 
        'is_published', 
        'get_playlist_ids'
        ]
    search_fields = ['title']
    list_filter = ['state', 'active']
    readonly_fields = ['id', 'is_published', 'get_playlist_ids']
    class Meta:
        model = VideoAllProxy
    
admin.site.register(VideoAllProxy, VideoAllProxyAdmin)


class VideoProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']
    # list_filter = ['video_id]
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, *args, **kwargs):
        return VideoPublishedProxy.objects.filter(active=True)

admin.site.register(VideoPublishedProxy, VideoProxyAdmin)