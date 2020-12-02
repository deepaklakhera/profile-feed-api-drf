from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer,UserProfileSerializer,ProfileFeedSerializer
from .models import UserProfile,ProfileFeedItem
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from . import permissions
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

class UserProfileFeedViewSet(viewsets.ModelViewSet):

    authentication_classes=(TokenAuthentication,)
    serializer_class=ProfileFeedSerializer
    queryset=ProfileFeedItem.objects.all()
    permission_classes=(
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self,serializer):
        """Sets the user profile to ligged in user"""
        serializer.save(user_profile=self.request.user)




class UserLoginApiView(ObtainAuthToken):
    """Handling creating user authentication token"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewSet(viewsets.ModelViewSet):
    
    
    queryset=UserProfile.objects.all()

    serializer_class=UserProfileSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpadateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class HelloApiView(APIView):

    serializer_class=HelloSerializer

    def get(self,request,format=None):
        """Returns a list of api"""
        
        an_apiview=[
            'Uses Http methods as function(get,post,patch,put,delete)',
            'is similar to django view',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):     
      
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"Hello {name}"
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles updating the object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial request of an object"""
        return Response({'method':'Patch'})

    def delete(self,request,pk=None):
        """Delete the object"""
        return Response({'method':'Delete'})

#viewsets -->simple CRUD,quick and simple api


class HelloViewSet(viewsets.ViewSet):

    serializer_class=HelloSerializer

    def list(self,request):

        a_viewset=[
            "Uses actions","LIST", "CREATE","RETREIVE","UpDATE"
        ]
        return Response({'message':'Hello',"a_viewset":a_viewset})

    def create(self,request):
        """Creates new Hello msg"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"Hello {name}!"
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retreive(self,request,pk=None):
        """Handle getting object by id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})