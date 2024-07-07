from django.urls import path, include

urlpatterns = [
    path('problem/', include('api.problem.urls')),
    path('terms/', include('api.terms.urls')),
    path('stats/', include('api.stats.urls')),
    path('user/', include('api.user.urls')),
]
