from django.db import models

# Create your models here.
class author(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    isActive=models.BooleanField(default=True)
    def to_dict(self):
        dic={
            
            'name':self.name,
            'id':self.id,
            'age':self.age,
            'email':self.email,
        }
        return dic
    class Meta:
        db_table='author'