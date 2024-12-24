from enroll.models import User
from enroll.api.serializer import UserSerializer
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
