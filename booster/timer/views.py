import datetime
import logging

from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.dateparse import parse_date
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from booster.timer.models import Timer
from booster.timer.serializers import TimerSerializer
from booster.utils.timezone import (get_day_end, get_day_start, get_today_end,
                                    get_today_start)

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
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)


    @action(detail=False, methods=['get'])
    def all_entry(self, request):
        """Get all the complete Time Enry"""
        if self.request.query_params.get('start') and self.request.query_params.get('end'):
            start_date = get_day_start(parse_date(self.request.query_params.get('start')))
            end_date = get_day_end(parse_date(self.request.query_params.get('end')))
        else:
            start_date = get_today_start()
            end_date = get_today_end()
        timers = self.queryset.filter(start_datetime__gte=start_date, start_datetime__lte=end_date)
        return Response(TimerSerializer(timers, many=True).data)


    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Perform For complete the Time Entry"""
        timer_obj = self.get_object()
        timer_obj.end_datetime = timezone.now()
        timer_obj.save()
        data = TimerSerializer(timer_obj).data
        logger.info("Time Entry" + str(timer_obj.pk) + "Completed Successfully")
        return Response({'status': 'Time Entry Ended Successfully'})


    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get all the incomplete  Time Enry"""
        start_date = get_today_start()
        end_date = get_today_end()
        active_timers = Timer.objects.filter(user=self.request.user, end_datetime=None)
        if  active_timers.exists():
            data = TimerSerializer(active_timers[0]).data
            return Response(data)
        else:
            logger.warning("Active entry doesn't exist'")
            return Response()
