from django import http


class CorsMiddleware(object):
    """Custom MiddleWare to set CORS Headers"""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """Adds neccessary headers to a response. This is automatically called on every request. 

        Args:
            request (dict): A python formatted http post request. 

        Returns:
            rest_framework.Response: A HTTP response containing specified headers. 
        """
        response = self.get_response(request)
        if (request.method == "OPTIONS"  and "HTTP_ACCESS_CONTROL_REQUEST_METHOD" in request.META):
            response = http.HttpResponse()
            response["Content-Length"] = "0"
            response["Access-Control-Max-Age"] = 86400
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        return response