from django.urls import reverse_lazy

ACCOUNT_AUTHENTICATION_METHOD = "username_email"

ACCOUNT_EMAIL_MAX_LENGTH = 40

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = ["none", "mandatory", "optional"][0]

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3

ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 900  # 15 minutes

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy("home:dashboard")

ACCOUNT_PRESERVE_USERNAME_CASING = False

ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

ACCOUNT_SIGNUP_REDIRECT_URL = reverse_lazy("home:edit-profile")

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USERNAME_MIN_LENGTH = 5

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"

ACCOUNT_USER_DISPLAY = lambda user: user.get_full_name() or user.username

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]