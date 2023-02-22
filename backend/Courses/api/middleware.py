class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Add custom header to the request
        request.META['MyHeader'] = 'Hello'
        response = self.get_response(request)
        return response