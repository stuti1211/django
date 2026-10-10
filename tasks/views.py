
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


@api_view(["GET"])
def task_list(request):
    tasks = Task.objects.all()

    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(["POST"])

def create_task(request):
    task_data = request.data
    serializer = TaskSerializer(data=task_data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=201)     

    else:
        return Response(serializer.errors,status=400)
