from posts.models.language import Language
from django.utils.deprecation import MiddlewareMixin

class ValidRequestMiddleware(MiddlewareMixin):

    def respond(self, request, message):
        response = self.get_response(request)
        response["Content-Type"] = "application/json"
        response.content = message
        return response

    def process_request(self, request):
        #VALIDATE IF REQUEST IS FROM FIREBASE
        response = self.get_response (request)
        return response
