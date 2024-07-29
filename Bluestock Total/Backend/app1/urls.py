
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'items', ItemViewSet)

urlpatterns = [
     path('',views.ok),
     path('', include(router.urls)),
     path('list/',views.ipo_list),
     path('content/<slug:val>',views.DetailView.as_view(),name='content'),
     
]
