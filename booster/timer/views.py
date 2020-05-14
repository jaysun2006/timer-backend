from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from booster.timer.models import Timer
from booster.timer.serializers import TimerSerializer
from django.utils import timezone


class TimerViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer

    def get_queryset(self):
        queryset = super(TimerViewSet, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if request.query_params.get('start'):
            queryset = queryset.filter(start_date=request.query_params.get('start'))
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)


    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        timer_obj = self.get_object()
        timer_obj.end_datetime = timezone.now()
        timer_obj.save()
        data = TimerSerializer(timer_obj).data
        return Response({'status': 'Time Entry Ended Successfully'})
