from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from main.libraries.serializers.ares_response_serializer import AresResponseSerializer
from main.libraries.utils import get_info_from_ares, validate_reg_number


class AresView(APIView):
    """
    View to show information about company based on registration number (IČO). Using ARES API.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="ARES auto completion view",
        responses={200: AresResponseSerializer()},
        manual_parameters=[openapi.Parameter("reg_number", openapi.IN_QUERY, type=openapi.TYPE_STRING)]
    )
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        reg_number = self.get_reg_number_from_request(request)

        try:
            validate_reg_number(reg_number)
        except ValidationError:
            return self.return_invalid_data()

        resp = get_info_from_ares(reg_number)
        if not resp:
            return self.return_invalid_data()

        return Response(resp)

    def get_reg_number_from_request(self, request):
        return request.GET.get('reg_number', None)

    def return_invalid_data(self):
        return Response(status=400, data={"reg_number": [_("neplatné IČ")]})
