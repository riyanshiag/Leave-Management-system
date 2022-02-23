
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class employee(models.Model):
    Manager='Manager'
    Employee='Employee'
    
    Position=(
        (Manager,'Manager'),
        (Employee,'Employee'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=False)
    profile=models.CharField(max_length=200,default=Employee,choices=Position)
    past_leaves=models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)],default=0)

    def __str__(self):
        return name
    
class leave(models.Model):
     name=models.CharField(max_length=200,null=False,blank=False)
     designation=models.CharField(max_length=200,null=False,blank=False)
     reason=models.CharField(max_length=1000)
     start_date=models.DateTimeField(null=False,blank=False,default=timezone.now)
     end_date=models.DateTimeField(null=False,blank=False)
     
     def __str__(self):
         return reason

    



