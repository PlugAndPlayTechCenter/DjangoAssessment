from django_assessment.startups.models import Startup
from django_assessment.startups.apps import StartupsConfig
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django_assessment.startups.serializers import StartupSerializer, UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class StartupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows startups to be viewed or edited.
    """
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [permissions.IsAuthenticated]
