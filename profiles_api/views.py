from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """TEST API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Return a list of APIView features"""
        an_apiview = [
            'User HTTP methods as functions (get, post, patch, put, delete)',
            'Is simailar to a tradiation Django View',
            'Gives you the most control over you appilcation logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name =  serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """Handle udating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an oject"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'Delete'})
