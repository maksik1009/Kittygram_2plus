import datetime

from rest_framework import throttling


class WorkingHoursRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if 6 <= now < 8:
            return False
        return True
