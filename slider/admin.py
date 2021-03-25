from django.contrib import admin
from django.utils import timezone

from slider.models import Slider


# Register your models here.
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('slider_name', 'is_publish', 'many_days_ago', 'created_at',)
    list_filter = ('is_publish',)
    ordering = ('slider_name', 'created_at',)
    search_fields = ('slider_name',)
    list_per_page = 15
    actions = ('publish','not_publish',)
    list_editable = ('is_publish',)

    def many_days_ago(self, obj):
        different = timezone.now().date() - obj.created_at.date()
        return different

    def publish(self, request, queryset):
        count = queryset.update(is_publish=True)
        self.message_user(request, f'{count} adet slider yayına alındı.')

    publish.short_description = 'İşaretlenen Sliderları Yayına Al'

    def not_publish(self, request, queryset):
        count = queryset.update(is_publish=False)
        self.message_user(request, f'{count} adet slider yayından çıkarıldı.')

    not_publish.short_description = 'İşaretlenen Sliderları Yayından Çıkar '
