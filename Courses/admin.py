from django.contrib import admin

from .models import Course, subscribe, Advert, Comment, Lesson, Material


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_course', 'slug_course', 'created_at', 'update_at')
    list_display_links = ('id', 'name_course')
    list_editable = ('slug_course',)
    list_per_page = 10
    search_fields = ('id', 'name_course', 'slug_course')

    # prepopulated_fields = {'slug_course': ('name_course',)}


# class MaterialInlineAdmin(admin.TabularInline):
#     model = Material


class MaterialInlineAdmin(admin.StackedInline):
    model = Material


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'name', 'release_data')
    search_fields = ('id', 'name', 'release_data')
    list_filter = ('course',)

    inlines = [
        MaterialInlineAdmin
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register([subscribe, Advert, Comment, Material])
admin.site.register(Lesson, LessonAdmin)
