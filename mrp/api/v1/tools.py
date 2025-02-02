from django.contrib.auth.hashers import make_password
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from profile.models import UserProfile


def create_profile(user, params):
    try:
        if user and user.is_authenticated:
            raise Exception("You are already logged in.")
        if UserProfile.objects.filter(email=params["email"]).exists():
            raise Exception("Please use another email address.")
        password = params["password"]
        password_again = params["password_again"]
        if password != password_again:
            raise Exception(
                "The passwords you entered are not the same. Please try again.."
            )
        else:
            try:
                password_validation.validate_password(password)
            except ValidationError:
                raise Exception("The passwords entered are not correct.")
            params["password"] = make_password(str(password))
            params.pop("password_again")
            profile = UserProfile(
                email=params["email"],
                password=params["password"],
                name=params["name"],
                surname=params["surname"],
                secret_answer=params["secret_answer"],
                type=params["type"],
            )
            profile.save()
    except Exception as ex:
        raise Exception(ex)


def check_user_is_valid(user, **kwargs):  # Must be one signal token validation
    if user is None:
        raise Exception("Your e-mail or password is incorrect, please try again.")
