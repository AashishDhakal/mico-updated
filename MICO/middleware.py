from users.models import ActivityLog
import json
from django.utils.functional import SimpleLazyObject
from django.conf import settings
from django.utils.cache import add_never_cache_headers
from .utils import get_user_agent


class BaseMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        pass


class UserAgentMiddleware(object):
    """
    middleware to return user agents information
    """

    def __init__(self, get_response=None):
        if get_response is not None:
            self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        request.user_agent = SimpleLazyObject(lambda: get_user_agent(request))


class UserActivityLogMiddleware(BaseMiddleware):
    """
    middleware to record user activity logs
    """

    def process_request(self, request):
        request.req_body = request.body

    def extract_log_info(self, request, response=None):

        log_data = {
            'ip_address': request.META['REMOTE_ADDR'],
            'request_method': request.method,
            'request_path': request.get_full_path(),
            'user': request.user,
        }
        if request.method in ['POST', 'PUT', 'PATCH']:
            try:
                log_data['request_body'] = json.loads(request.req_body)
            except json.JSONDecodeError:
                log_data['request_body'] = 'Request body not in Json Format'
            if response:
                response_body = response.status_code
                log_data['response_body'] = response_body
                log_data['ip_address'] = request.META['REMOTE_ADDR']
                log_data['browser_used'] = str(request.user_agent.browser.family) + ' ' \
                                           + str(request.user_agent.browser.version_string)
                log_data['device_used'] = request.user_agent.device.family
        elif request.method == 'GET':
            log_data['request_body'] = request.META['QUERY_STRING']
            if response:
                response_body = response.status_code
                log_data['response_body'] = response_body
                log_data['ip_address'] = request.META['REMOTE_ADDR']
                log_data['browser_used'] = str(request.user_agent.browser.family) + ' ' \
                                           + str(request.user_agent.browser.version_string)
                log_data['device_used'] = request.user_agent.device.family
        return log_data

    def process_response(self, request, response):
        if request.method in ['GET', 'POST', 'PUT', 'PATCH']:
                log_data = self.extract_log_info(request=request, response=response)
                if response.status_code in range(200, 300):
                    if request.user.is_authenticated:
                        ActivityLog.objects.create(
                            user=request.user, method=request.method, data=log_data['request_body'],
                            url_path=request.get_full_path(), status_code=log_data['response_body'],
                            ip_address=log_data['ip_address'], browser_used=log_data['browser_used'],
                            device_used=log_data['device_used']
                        )
                    else:
                        ActivityLog.objects.create(
                            method=request.method, data=log_data['request_body'],
                            url_path=request.get_full_path(), status_code=log_data['response_body'],
                            ip_address=log_data['ip_address'], browser_used=log_data['browser_used'],
                            device_used=log_data['device_used']
                        )
        return response

class DisableClientSideCachingMiddleware :

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return self.process_response(request, response)

    def process_response(self, request, response):
        add_never_cache_headers(response)
        if settings.CLEAR_BROWSER_CACHE:
            response["Pragma"] = "no-cache"
            response["Expires"] = "-1"
            response["Strict-Transport-Security"]: "max-age=0"
        return response
