# from rest_framework.routers import DefaultRouter
from booster.timer.views import TimerViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'timer', TimerViewSet)
