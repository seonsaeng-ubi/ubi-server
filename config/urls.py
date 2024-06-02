from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg import openapi
import os


class SchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super(SchemaGenerator, self).get_schema(request, public)
        schema.basePath = os.path.join(schema.basePath, '')
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="UBI API Swagger",
        default_version="v1",
        description="선생우비 API 문서",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    # generator_class=SchemaGenerator,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),

    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = f'{settings.SITE_NAME} Admin'
admin.site.site_title = f'{settings.SITE_NAME}'
