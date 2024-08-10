from api.problem.models import Region, BigSubject, SmallSubject, Problem, Color, TestSet, RealRegion
from django.contrib import admin


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'title', 'number')
    list_display_links = ('title',)
    list_filter = ['title']
    search_fields = ('title', 'user',)
    summernote_fields = []

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.request = request
        return form

    def get_id(self, obj):
        return obj.id

    get_id.short_description = 'ID'


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'title',)

    def get_id(self, obj):
        return obj.id

    get_id.short_description = 'ID'


@admin.register(RealRegion)
class RealRegionAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'title',)

    def get_id(self, obj):
        return obj.id

    get_id.short_description = 'ID'


@admin.register(BigSubject)
class BigSubjectAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'title',)

    def get_id(self, obj):
        return obj.id

    get_id.short_description = 'ID'


@admin.register(SmallSubject)
class SmallSubjectAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'title',)

    def get_id(self, obj):
        return obj.id

    get_id.short_description = 'ID'


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'title',)

    def get_id(self, obj):
        return obj.id

    get_id.short_description = 'ID'


@admin.register(TestSet)
class TesttSetAdmin(admin.ModelAdmin):
    pass
