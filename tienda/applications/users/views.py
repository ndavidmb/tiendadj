from django.shortcuts import render

from rest_framework.views import APIView

from django.views.generic import TemplateView

from .serializers import LoginSocialSerializer
# Create your views here.

class LoginUser(TemplateView):
    template_name = "users/login.html"

class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        id_token = serializer.data.get('token_id')

        
        return None