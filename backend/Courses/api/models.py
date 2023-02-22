from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    taken_by = models.ManyToManyField(User, related_name='taken_by')

    def __str__(self):
        return self.name
    
#Elegí este enfoque frente a una tabla de relación clásica ya que 
# probablemente el usuario tenga otros campos a agregar en un futuro
# (si el ejercicio continuase)
class Custom_user(User):
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.username
    
    
# Models:
# -User
# -Course
# -Lesson

# Relationships:
# Friendship(user-user)
# Lesson-course
# User-Lesson