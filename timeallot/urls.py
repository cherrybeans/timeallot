"""
timeallot URL Configuration
"""

from django.conf.urls import url, include
from django.conf import settings
from rest_framework import routers

from timeallot.apps.user import views as userviews
from timeallot.apps.timer import views as timerviews


router = routers.DefaultRouter()
router.register(r'users', userviews.UserViewSet)
router.register(r'categories', timerviews.CategoryViewSet)
router.register(r'projects', timerviews.ProjectViewSet)
router.register(r'subtags', timerviews.SubtagViewSet)
router.register(r'sessions', timerviews.SessionViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]