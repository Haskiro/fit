from .services import log_visit, write_visit_log
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(write_visit_log, 'interval', minutes=1)
scheduler.start()

class VisitLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin') and not request.path.startswith('/auth') and not request.path.startswith('/static'):
          log_visit(request)
        response = self.get_response(request)
        return response