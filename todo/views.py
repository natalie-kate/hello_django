from django.shortcuts import render

# Create your views here.


def get_todo_list(request):
    return render(request, 'todo_templates/todo_list.html')
