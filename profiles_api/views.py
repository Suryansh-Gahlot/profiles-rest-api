from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """TEST API View"""
    def get(self, request, format = None):
        """Return a list of APIView features"""
        an_apiview = [
            'User HTTP methods as functions (get, post, patch, put, delete)',
            'Is simailar to a tradiation Django View',
            'Gives you the most control over you appilcation logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
