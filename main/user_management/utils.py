from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from ..models import User

def _userExist(email, username):
    try:
        User.objects.get(Q(email = email) | Q(username = username))
        return 1
    except Exception as e:
        if isinstance(e, User.DoesNotExist):
            return 0
        else:
            raise serializers.ValidationError(
                'Username or email already used by another contributor.'
            )


def _createUser(email, username):
    newUser = User.objects.create(email = email, username = username)
    newUser.save()
    return newUser


def _getUser(email, username):
    return User.objects.get(email = email, username = username)

    
