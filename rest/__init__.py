# $ python manage.py shell
# >>> from rest_framework.authtoken.models import Token

# >>> from django.contrib.auth.models import User

# >>> user = User.objects.get(id=1)

# >>> user
# <User: admin>

# >>> token = Token.objects.create(user=user)

# >>> token
# <Token: 94fc6b43208a8b71bcb1f37e155e4ee05e61ea46>

