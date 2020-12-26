from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Users GET/POST': '/users/',
        'User GET/PUT/DELETE': '/user/<str:pk>/',
    }
    return Response(api_urls)