
from rest_framework.serializers import ModelSerializer
from booster.timer.models import Timer


class TimerSerializer(ModelSerializer):
    class Meta:
        model = Timer
        fields = '__all__'
