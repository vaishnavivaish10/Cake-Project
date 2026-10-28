from django.db import models

# Create your models here.

# class CategoryChoices(models.TextChoices):

#     BIRTHDAY_CAKE='Birthday Cake','Birthday Cake'

#     WEDDING_CAKE='Wedding cake','Wedding cake'

# class WeightChoices(models.TextChoices):

#     HALF_KG='1/2 kg','1/2 kg'

#     ONE_KG='1 kg','1 kg'

#     TWO_KG='2 kg','2 kg'

# class ShapeChoices(models.TextChoices):

#     RECTANGLE='Rectangle','Rectangle'

#     ROUND='Round','Round'

class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
    
            return self.name
    
    class Meta :
    
            verbose_name='Categories'
    
            verbose_name_plural='Categories'

class Weight(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
    
            return self.name
    
    class Meta :
    
            verbose_name='weight'
    
            verbose_name_plural='weight'

class Shape(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
    
            return self.name
    
    class Meta :
    
            verbose_name='Shape'
    
            verbose_name_plural='Shape' 

class Cake(models.Model):

    name=models.CharField(max_length=25)

    description=models.TextField()

    photo=models.ImageField(upload_to='cake-image')

    category=models.ForeignKey('Category',on_delete=models.CASCADE)

    weight=models.ForeignKey('Weight',on_delete=models.CASCADE)

    shape=models.ForeignKey('Shape',on_delete=models.CASCADE)

    price=models.FloatField()

    def __str__(self):

        return self.name

    class Meta :

        verbose_name='Cakes'

        verbose_name_plural='Cakes'

    