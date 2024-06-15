from api.problem.models import Problem, ProblemSet, Region, BigSubject, SmallSubject
from django.contrib import admin


@admin.register(ProblemSet)
class ProblemSetAdmin(admin.ModelAdmin):
    pass


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(BigSubject)
class BigSubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(SmallSubject)
class SmallSubjectAdmin(admin.ModelAdmin):
    pass
