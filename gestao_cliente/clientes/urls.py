from django.urls import path
from .views import persons_list
#from .views import teste_unit
from .views import persons_new
from .views import persons_update
from .views import persons_delete

urlpatterns = [
    path('list/', persons_list, name="person_list"),
   # path('teste/', teste_unit),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
]