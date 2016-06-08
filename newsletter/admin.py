from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'timestamp', 'updated']
    # when creating custom forms, you need to reference the forms.py,
    # and set the variable 'form' (built-in) to the chosen class inside of forms.py
    form = SignUpForm

# register the class, with the SignUp model as input
admin.site.register(SignUp, SignUpAdmin)