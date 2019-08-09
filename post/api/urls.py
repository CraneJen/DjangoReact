from rest_framework import routers
from post.api.views import PostViewSet
# from django.urls import path
router = routers.DefaultRouter()
router.register(r'', PostViewSet, 'post')
urlpatterns = router.urls
