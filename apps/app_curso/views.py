from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Course, Description,Comentario

# Create your views here.
def index(request):
    context = {
        "cursos" : Course.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST,"create")
        if len(errors) > 0:
            return JsonResponse(errors)
        name = request.POST["name"]
        description = request.POST["description"]
        course = Course.objects.create(name=name,description=Description.objects.create(description=description))
        return JsonResponse({"resultado": course.id })

def predestroy(request,id):
        context = {
            "curso" : Course.objects.get(id=id),
        }
        return render(request, "destroy.html",context)

def destroy(request,id):
    curso = Course.objects.get(id=id)
    curso.delete()
    return redirect("/")

def comment(request,id):
    context = {
            "datos" : Course.objects.get(id=id),
            "comentarios" : Comentario.objects.filter(curso=id),
        }
    return render(request, "comments.html",context)

def create_comment(request,idCurso):
     if request.method == "POST":
        comment = request.POST["comment"]
        Comentario.objects.create(comentario=comment,curso=Course.objects.get(id=idCurso))
        return redirect(f"/courses/comment/{idCurso}")