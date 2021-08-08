from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) <= 5:
            errors["title"] = "El nombre debe tener mas de 5 caracteres"
        if len(postData['description']) < 15 or len(postData['description']) > 30:
             errors["description"] = "Description debe tener minimo 15 caracteres y maximo 30 caracteres"
        return errors

# Create your models here.
class Description(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.OneToOneField(Description,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class ComentarioManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 5:
            errors["title"] = "El nombre debe tener mas de 5 caracteres"
        return errors


class Comentario(models.Model):
    comentario = models.TextField()
    curso = models.ForeignKey(Course, related_name="cursos", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ComentarioManager()