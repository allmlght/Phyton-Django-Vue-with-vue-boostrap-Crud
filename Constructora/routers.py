from rest_framework import routers
from polls.viewsets import ArticleViewSet
router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)