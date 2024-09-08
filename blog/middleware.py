# middleware.py

from django.shortcuts import render

class Custom403Middleware:
    """
    Middleware to handle 403 Forbidden errors with a custom template.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # This code is executed for each request before the view is called.

        response = self.get_response(request)

        # This code is executed for each request/response after the view is called.
        if response.status_code == 403:
            # Render the custom 403 template
            return render(request, 'admin/403.html', status=403)

        return response
