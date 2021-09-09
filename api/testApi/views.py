from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Form
from .serializers import FormSerializer
from pdfminer.high_level import extract_text


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List-Form-Data': '/list/',
        'Detail-Form-Data': '/detail/<str:id>/',
        'Create-Form-Data': '/create/'
    }
    return Response(api_urls)


@api_view(['GET'])
def listForms(request):
    forms = Form.objects.all()
    serializer = FormSerializer(forms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def selectForm(request, key):
    forms = Form.objects.get(id=key)
    serializer = FormSerializer(forms, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createForm(request):
    serializer = FormSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
