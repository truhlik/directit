from rest_auth.registration.views import RegisterView
from rest_framework import viewsets, authentication, permissions, mixins
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer, ClientUserRegistrationSerializer, ConsultantRegistrationSerializer,\
    SupplierRegistrationSerializer


class UserViewSets(mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super(UserViewSets, self).get_queryset().owner(self.request.user).prefetch_related('companies')

    @action(methods=['get', 'patch'], detail=False)
    def self(self, request, *args, **kwargs):
        self.kwargs.update({'pk': self.get_queryset().first().id})
        if request.method == 'PATCH':
            return self.partial_update(request, *args, **kwargs)
        elif request.method == 'PUT':
            return self.update(request, *args, **kwargs)
        else:
            return self.retrieve(request, *args, **kwargs)


class ClientRegisterView(RegisterView):
    serializer_class = ClientUserRegistrationSerializer


class ConsultantRegisterView(RegisterView):
    serializer_class = ConsultantRegistrationSerializer


class SupplierRegisterView(RegisterView):
    serializer_class = SupplierRegistrationSerializer
