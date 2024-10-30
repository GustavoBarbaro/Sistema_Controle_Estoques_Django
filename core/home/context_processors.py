from django.utils.timezone import now
from datetime import datetime


def current_datetime(request):
    return {'today': datetime.today()}
