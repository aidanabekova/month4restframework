from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User  # для регистрации юзера


@api_view(['POST'])
def register(request):
    if request.method == 'POST':  # это у нас регистрация
        # username = request.data['username']
        # password = request.data['password']
        User.objects.create_user(**request.data)
        return Response(data={'user created'}, status=201)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':  # это у нас авторизация
        # username = request.data['username']   #эти две строки можно написать в одну строку(как внизу)
        # password = request.data['password']
        user = authenticate(**request.data)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'token': token.key})
        return Response(data={'user not found'}, status=404)
