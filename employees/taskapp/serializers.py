from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Comment, Employee,Role
from rest_framework import permissions

from django.contrib.auth.models import User, Group
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'task','time','completed']
        






class CommentSerializer(serializers.HyperlinkedModelSerializer):
    # permission_classes = (permissions.IsAuthenticated,)
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(CommentSerializer, self).__init__(many=many, *args, **kwargs)



    class Meta:
        model = Comment
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
