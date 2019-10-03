from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets
from tasks.models import Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(
        many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'tasks']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
