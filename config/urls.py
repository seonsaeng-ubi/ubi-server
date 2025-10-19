from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg import openapi
from api.problem.views import AssetLinksView, AppleAppSiteAssociationView, StudyRoomDeepLinkResolveAPIView
from api.user.views import AppleSIWANotificationView
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
    # well-known for app/universal links
    path('.well-known/assetlinks.json', AssetLinksView.as_view(), name='assetlinks'),
    path('.well-known/apple-app-site-association', AppleAppSiteAssociationView.as_view(), name='apple-app-site-association'),
    # 일부 iOS 클라이언트 호환(루트에서도 제공)
    path('apple-app-site-association', AppleAppSiteAssociationView.as_view(), name='apple-app-site-association-root'),

    # Deep Link Resolver (Universal/App Links)
    path('s/study/room/<str:token>/', StudyRoomDeepLinkResolveAPIView.as_view(), name='deeplink-resolve'),
    # 기존 단축 경로도 병행 지원 (하위 호환)
    path('s/<str:token>/', StudyRoomDeepLinkResolveAPIView.as_view(), name='deeplink-resolve-legacy'),

    # Sign in with Apple Server-to-Server notifications (root path)
    path('apple/siwa/notifications', AppleSIWANotificationView.as_view(), name='siwa-s2s-no-slash'),
    path('apple/siwa/notifications/', AppleSIWANotificationView.as_view(), name='siwa-s2s'),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('summernote/', include('django_summernote.urls')),
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = f'{settings.SITE_NAME} Admin'
admin.site.site_title = f'{settings.SITE_NAME}'
