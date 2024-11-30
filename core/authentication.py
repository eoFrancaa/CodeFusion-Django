from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from firebase_admin import auth
from django.http import JsonResponse

class FirebaseJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            return None

        token = token.split(' ')[1]

        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token.get('name')
            return (self.get_or_create_user(uid, decoded_token), None)
        except Exception as e:
            raise AuthenticationFailed(f"Token inválido: {str(e)}")

    def get_or_create_user(self, uid, decoded_token):
        from core.models import User

        email = decoded_token.get('email')
        user, created = User.objects.get_or_create(
            name=uid,
            defaults={'email': email},
        )
        return user


class FirebaseAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extrai o token do cabeçalho Authorization
        auth_header = request.META.get('HTTP_AUTHORIZATION', None)
        if auth_header:
            parts = auth_header.split()

            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                try:
                    # Verifica o token no Firebase
                    decoded_token = auth.verify_id_token(token)
                    request.user = decoded_token  # Armazena os dados do usuário no request
                except Exception as e:
                    return JsonResponse({"error": "Invalid token"}, status=401)
        
        return self.get_response(request)
