from api.problem.models import ProblemSet, Region, BigSubject, SmallSubject, Problem, Summernote
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe
from django.contrib import admin
from django import forms
import re


class ProblemAdminForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = '__all__'

    def save(self, commit=True):
        try:
            instance = super().save(commit=False)
            instance.save()

            content = self.cleaned_data['content']
            img_contents = re.findall(r'django-summernote/.*?"', content)
            for img in img_contents:
                imgs_path = img[0:len(img) - 1]
                summernote = Summernote.objects.get(file=imgs_path)
                summernote.document = instance
                summernote.save()
        except:
            instance = super().save(commit=False)

        return instance


@admin.register(ProblemSet)
class ProblemSetAdmin(admin.ModelAdmin):
    pass


@admin.register(Problem)
class ProblemAdmin(SummernoteModelAdmin):
    form = ProblemAdminForm
    list_display = ('get_id', 'title',)
    list_display_links = ('title',)
    list_filter = ['title']
    search_fields = ('title', 'user',)
    summernote_fields = ('presentation', )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.request = request
        return form

    def get_id(self, obj):
        return obj.id

    get_id.short_description = 'ID'


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(BigSubject)
class BigSubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(SmallSubject)
class SmallSubjectAdmin(admin.ModelAdmin):
    pass
