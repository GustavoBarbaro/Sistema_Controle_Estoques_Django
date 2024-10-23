from django.contrib.auth.forms import UserCreationForm
from estoque.models import Usuario  

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario  
        fields = ('username',)
