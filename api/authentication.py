from rest_framework.authentication import TokenAuthentication as TokenBaseAuth

class TokenAuthentication(TokenBaseAuth):
    keyword = 'Bearer'

