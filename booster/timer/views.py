import logging
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from booster.timer.models import Timer
from booster.timer.serializers import TimerSerializer
from django.utils import timezone

logger = logging.getLogger(__name__)



class TimerViewSet(viewsets.ModelViewSet):
    """
    A viewset that provide:
    For listing Time Entry
    For Creating Time Entry
    For details of Time Entry
    For deleting Time Entry
    For updating Time Entry
    
    """
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer

    def get_queryset(self):
        queryset = super(TimerViewSet, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if self.request.query_params.get('start'):
            queryset = queryset.filter(start_date=request.query_params.get('start'))
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)


    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Perform For complete the Time Enry"""
    
        timer_obj = self.get_object()
        timer_obj.end_datetime = timezone.now()
        timer_obj.save()
        data = TimerSerializer(timer_obj).data
        logger.info("Time Entry" + str(timer_obj.pk) + "Completed Successfully")
        return Response({'status': 'Time Entry Ended Successfully'})
