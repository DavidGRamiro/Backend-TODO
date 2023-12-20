from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)

        # Verificar si el token está desactivado
        if not token: 
            raise AuthenticationFailed('Neceitas loguearte primero')

        return user, token