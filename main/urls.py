from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

from allauth.account.views import ConfirmEmailView

from main.apps.users.views import ClientRegisterView, ConsultantRegisterView, SupplierRegisterView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="DirectIT API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="lubos@endevel.cz"),
      license=openapi.License(name="Endevel License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # tyhle view handluje front a jsou zde jen dummy pro reverse url
    path('#/login', TemplateView.as_view(template_name='frontend.html'), name='login'),
    path('#/new-password', TemplateView.as_view(template_name='frontend.html'), name='fronted_password_reset'),
    path('#/projekty/<int:id>/upravit', TemplateView.as_view(template_name='frontend.html'), name='frontend_project_detail'),

    # tady už jsou backend URL
    path('accounts/', include('allauth.urls')),
    path('api/v1/', include('main.libraries.urls')),
    path('api/v1/', include('main.api_urls')),
    path('api/v1/accounts/', include('rest_auth.urls')),
    path('api/v1/accounts/registration/client/', ClientRegisterView.as_view(), name='registration-client'),
    path('api/v1/accounts/registration/consultant/', ConsultantRegisterView.as_view(), name='registration-consultant'),
    path('api/v1/accounts/registration/supplier/', SupplierRegisterView.as_view(), name='registration-supplier'),
    path('api/v1/accounts/registration/', include('rest_auth.registration.urls')),

    # standardní view na zprocesování potvrzení mailové adresy
    path('admin/accounts/confirm/<key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),

    path('admin/', admin.site.urls),
    path(r'swagger<str:format>\.json|\.yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
