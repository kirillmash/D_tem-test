from django.utils.cache import patch_vary_headers


class AddHelloWorldInHeaderMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        body = str(response.content, 'utf-8')
        new_body = body.replace('</head>', '<!-HelloWorld>></head>')
        response.content = new_body.encode('utf-8')
        return response
