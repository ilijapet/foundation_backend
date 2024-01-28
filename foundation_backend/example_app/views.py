from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):

    def get(self, request):
        return Response({"message": "Hello, world!"})
