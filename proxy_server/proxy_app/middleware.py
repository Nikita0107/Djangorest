class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Ваш код логирования запросов
        response = self.get_response(request)
        return response