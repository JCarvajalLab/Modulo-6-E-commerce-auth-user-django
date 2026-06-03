from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    ##Se quita el mensaje de ayuda, si se comenta vuelve a aparecer todo
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text = None