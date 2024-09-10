from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 255, blank= False, null=False)
    description = models.TextField(max_length= 300, blank= True, null= True)
    price = models.DecimalField(max_digits= 10, decimal_places= 2, default= 0.0)
    # image = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.title

    @property #? this allows us to use the function as a attribute of the class object so we can call it without using parenthesis
    def sale_price(self):
        return self.price *5
