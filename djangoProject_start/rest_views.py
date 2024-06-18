#with django rest framework


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from djangoProject_start.models import User
from djangoProject_start.serializer import userSerializer

#we have to provide two things queryset and serializer where query set is model which we need and serializer is
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class= userSerializer


class UserRetrieveDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    lookup_field = 'id'
