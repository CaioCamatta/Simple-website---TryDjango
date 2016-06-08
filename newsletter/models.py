from django.db import models

# Create your models here.
class SignUp(models.Model):
    # EmailField is the same thing as a CharField, but it checks if the entered value is a valid email
    email = models.EmailField()
    # if null is true django will store NULL in the database
    full_name = models.CharField(max_length=120)
    # when its created, automatically set its time. it cannot be changed. will not be changed when saved
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # will be changed when saved
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # representation of the model. its what you see in the admin
    def __str__(self):
        return self.email
