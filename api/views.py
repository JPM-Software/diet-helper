from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Users GET/POST': '/users/',
        'User GET/PUT/DELETE': '/users/<str:pk>/',
        'User Details GET/PUT': '/users/<str:pk>/details',
        'Foods GET/POST': '/foods/',
        'Food GET/PUT/DELETE': '/foods/<str:pk>/',
    }
    return Response(api_urls)