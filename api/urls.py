from django.conf.urls import url

from forumdireito_app.views import *

helper_patterns = [
   url(r'^palestras/$', PalestrasList.as_view(), name="palestras"),
   url(r'^perguntas/$', PerguntaList.as_view(), name="perguntas"),
]
urlpatterns = helper_patterns
