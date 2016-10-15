from django.conf.urls import url, include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todo', views.TodoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
