from django.conf.urls import url
from users.views import *


urlpatterns = [
    url(r'^signup', SignUp.as_view(), name="signup"),
    url(r'^login', Login.as_view(), name="login"),
]