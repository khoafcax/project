
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.serializers import Serializer
from .models import Note, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
from .models import Product
from .serializers import NoteSerializer
from api import serializers
# from api import serializers
# from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote
# Create your views here.
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many= False)
    return Response(serializer.data)



@api_view(['POST'])
def testNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many= False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    note= Note.objects.get(id=pk)
    serializer = NoteSerializer(instance =note, data =data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response ("Note was deleted")


@api_view(['POST', 'GET'])
def  createProduct(request):
    if request.POST.get('action') == 'create-post':
        name= request.POST.get('name')
        temp = request.POST.get('content')
        content =temp.split()
        print("Tao la Khoa")
        serializer = NoteSerializer()
        test = list(Product.objects.filter(user="tit").values('content'))
        ex = [d['content'] for d in test]
        for i in range(len(content)):
            titi= content[i]
           
            # print (tempp)
            if titi not in ex:
                if (len(titi) == 5) and (titi.isalpha()):
                    obj =Product.objects.create(
                    user =name,
                    content = titi )
                    print(type(Product))
                    # objj = eval(tempp).objects.create(
                    # word = titi )
                    serializer = NoteSerializer(obj)
                    print("Everything will be ok")
                else:
                    print("NOT NOT NOT GOOD")
                    print(titi)
            
            else:
                print("The word " + str(titi) +" is already in list")
            
            first_letter = titi[0].upper()
            temp_letter = list(eval(first_letter).objects.values('word'))
            exx = [d['word'] for d in temp_letter]
            print(exx)
            print("* "*30)
            if titi not in exx:
                if (len(titi) == 5) and (titi.isalpha()):
                    objj = eval(first_letter).objects.create(
                    word = titi )
                    serializer = NoteSerializer(objj)
                    print("Everything will be ok nhe")
                else:
                    print("NOT NOT NOT GOOD")
                    print(titi)
            else: 
                None
            
            print("* "*15)
            
        # serializer = NoteSerializer(obj)

            
        print("* "*15)
        print(test)
        print("Khoa Pham")
        print(type(test))
        # res = [ sub['content'] for sub in test }
        # print(res)
        print("* "*20)
        print(ex)
        print("* "*30)

        # serializer = NoteSerializer(Product.name,Product.content, many= True)
        return Response(serializer.data)
    return Response("Tao Bi Loi")

@api_view(['POST'])
def  createUser(request):
    if request.POST.get('action') == 'create-post':
        # name= request.POST.get('name')
        temp = request.POST.get('content')
        content =temp.split()
        titi= content[2]
        obj =Product.objects.create(
            # name =name,
            content = titi
        )
        
        serializer = NoteSerializer(obj)

        print("khoaPham")
        # serializer = NoteSerializer(Product.name,Product.content, many= True)
        return Response(serializer.data)
    return Response("Tao Bi Loi")