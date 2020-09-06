#from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
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


# viewset이란?
# 단일클래스에 관련있는 view들을 결합한 것이 viewset
# 여러가지 API의 기능을 통합해서 하나의 API Set로 제공한다. 
# 하나의 모델을 가지고 각각의 API를 만들게 되면 중복되는 로직이 많기 때문에 ViewSet를 사용함으로써 코드의 효율성을 높일 수 있다. 

# viewset을 위한 method 핸들러들은 as_view()함수를 사용해 view가 끝나는 시점에 해당하는 행동을 취할 때 바인딩함
# .list(), .create() 같은 액션 제공