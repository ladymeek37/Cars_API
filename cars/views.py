# Create your views here.
# Where we define all the functions the outside world can interact with through urls over the internet.
# Decorator is going to assign certian permissions to that function.
# Here we will define what request types that function is capable of handling.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def cars_list(request):
    

    return Response('ok')