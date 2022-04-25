from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from todo.models import Todo
from .serializers import ItemSerializer, TodoSerializer


@api_view(['GET'])
def getDataDummy (request):
    if request.method == 'GET':
        return Response({'data': 'Hello World', 'message': 'Success'})
    
    
@api_view(['GET'])
def getData (request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def addItem (request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET'])
def getTodo (request):
    if request.method == 'GET':
        items = Todo.objects.all()
        serializer = TodoSerializer(items, many=True)
        return Response(serializer.data)    
    
@api_view(['GET'])
def getTodoDetail (request, pk):
    if request.method == 'GET':
        items = Todo.objects.get(pk)
        serializer = TodoSerializer(items, many=False)
        return Response(serializer.data)      
 
@api_view(['POST'])
def addTodo (request):
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)   
    
@api_view(['POST'])
def updateTodo (request, pk):
    if request.method == 'POST':
        items = Todo.objects.get(id=pk)
        serializer = TodoSerializer( instance=items ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)       