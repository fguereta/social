from django.conf.urls import include, url
from aplicacion import views


urlpatterns = [
    
    url(r'^registrarpersona$', views.crear, name='crear'),
    
        
   
]
