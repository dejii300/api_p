from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('paradigns', views.ParadignView)
router.register('programmers', views.ProgrammerView)

urlpatterns = [
    path('', include(router.urls))
]