from django.contrib.auth.models import User, Group
from .models import Comment, Employee,Role
from rest_framework import viewsets
from rest_framework import permissions
from taskapp.serializers import UserSerializer,GroupSerializer, EmployeeSerializer, CommentSerializer,RoleSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer


class UserViewSet(viewsets.ModelViewSet):
  
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
  
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'role']

    # renderer_classes = [XLSXRenderer]
    # filename = 'my_export.xlsx'


# class CommentViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticated]
    # ,XLSXFileMixin,ReadOnlyModelViewSet

class CommentViewSet(viewsets.ModelViewSet,XLSXFileMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author']
    # renderer_classes = [XLSXRenderer]
    # filename = 'my_export.xlsx'
   
class CommentList(APIView):
    renderer_classes = [XLSXRenderer]
    filename = 'my_export.xlsx'
    

    def get(self, request,format=None):
        comments = Comment.objects.all()
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)
class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]        
class RoleDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'taskapp/role_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(Role, pk=pk)
        serializer = RoleSerializer(role)
        return Response({'serializer': serializer, 'role': Role})

    def post(self, request, pk):
        role = get_object_or_404(Role, pk=pk)
        serializer = ProfileSerializer(role, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'role': role})
        serializer.save()
        return redirect('profile-list')
# class RoleList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
   

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)