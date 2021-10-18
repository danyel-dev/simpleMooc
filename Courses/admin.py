from django.contrib import admin

from .models import Course, subscribe, Advert, Comment


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_course', 'slug_course', 'created_at', 'update_at')
    list_display_links = ('id', 'name_course')
    list_editable = ('slug_course',)
    list_per_page = 10
    search_fields = ('id', 'name_course', 'slug_course')

    # prepopulated_fields = {'slug_course': ('name_course',)}


admin.site.register(Course, CourseAdmin)
admin.site.register(subscribe)
admin.site.register(Advert)
admin.site.register(Comment)
