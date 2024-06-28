from django.urls import path, include

urlpatterns = [
    path('user/', include('api.user.urls')),
    path('problem/', include('api.problem.urls')),
    path('terms/', include('api.terms.urls')),
]
