from django.utils.cache import patch_vary_headers


class AddHelloWorldInHeaderMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        body = response.content
        new_body = body.replace(b'</head>', b'<!-HelloWorld></head>')
        response.content = new_body
        return response
