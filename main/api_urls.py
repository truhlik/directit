from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.apps.companies import views as company_views
from main.apps.tags import views as tag_vies
from main.apps.categories import views as category_views
from main.apps.users import views as user_views
from main.apps.callbacks import views as callback_views
from main.apps.testimonials import views as testimonial_views
from main.apps.software import views as software_views
from main.apps.orders import views as order_views
from main.apps.projects import views as project_views
from main.apps.files import views as files_views
from main.apps.messages import views as message_views
from main.apps.services import views as services_views
from main.apps.products import views as products_views
from main.apps.reference import views as reference_views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('companies', company_views.CompanyViewSet, basename='company')
router.register('suppliers', company_views.SupplierViewSet, basename='supplier')
router.register('consultants', company_views.ConsultantViewSet, basename='consultant')
router.register('tags', tag_vies.TagViewSet)
router.register('categories', category_views.CategoryViewSet)
router.register('users', user_views.UserViewSets)
router.register('callbacks', callback_views.CallbackViewSet)
router.register('consierge', callback_views.ConsiergeViewSet, basename='consierge')
router.register('assistant', callback_views.ITAssistantViewSet, basename='assistant')
router.register('testimonials', testimonial_views.TestimonialViewSet)
router.register('software', software_views.SoftwareViewSet)
router.register('orders', order_views.OrderViewSet)
router.register('projects', project_views.ProjectViewSet)
router.register('files', files_views.FilesViewSets)
router.register('services', services_views.ServiceViewSet, basename='service')
router.register('products', products_views.ProductViewSet)
router.register('messages', message_views.MessageViewSet)
router.register('references', reference_views.ReferenceViewSet, basename='reference')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('categories/group/', category_views.CategoryGroupByViewSet.as_view()),
    path('', include(router.urls)),
]
