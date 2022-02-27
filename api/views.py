from cgitb import reset
from os import stat
from urllib import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import  Section
from .serializers import SectionSerializer


class SectionView(APIView):
    
    #get all sections and subsections
    def get(self, request):
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)

    def post(self, request):
        response = {"message":"", "data":[]}
        # Create an article from the above data
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        response["message"] = "section created successfully"
        response["data"] = serializer.data
        return Response(response, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        response =  {"error":"","message":""}
        try:
            section_update = Section.objects.get(id=pk)
            serializer = SectionSerializer(instance=section_update, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except Exception as why:
            response['error'] = str(why)
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
        response["message"] =  "updated successfully"
        response["data"] = serializer.data
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        response = {"message":"","error":""}
        try:
            section = Section.objects.get(id=pk)
            section.delete()
            print("xxxxx")
        except Exception as why:
            response['error'] = str(why)
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        response["message"] = f"Article with id {pk} has been deleted"
        return Response(response, status=status.HTTP_204_NO_CONTENT)
