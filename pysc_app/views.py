from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Question,Test
from .serializers import QuestionSerializer,TestSerializer
from rest_framework.response import Response
from rest_framework import status


class QuestionViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()
    lookup_field = 'content'

    def list(self, request):
        serializer = QuestionSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self,request,content):
        question = get_object_or_404(self.queryset, content=content)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def update(self,request,content):
        question = get_object_or_404(self.queryset,content=content)
        serializer = QuestionSerializer(question,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(question,serializer.validated_data)
        return Response(serializer.data)

    def partial_update(self,request,content):
        question = get_object_or_404(self.queryset,content=content)
        serializer = QuestionSerializer(question,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(question,serializer.validated_data)
        return Response(serializer.data)
    
    def destroy(self,rquest,content):
        question = get_object_or_404(self.queryset,content=content)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestViewSet(viewsets.ViewSet):
    queryset = Test.objects.all()
    lookup_field = 'name'

    def list(self, request):
        serializer = TestSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = TestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self,request,name):
        test = get_object_or_404(self.queryset, name=name)
        serializer = TestSerializer(test)
        return Response(serializer.data)

    def update(self,request,name):
        test = get_object_or_404(self.queryset,name=name)
        serializer = TestSerializer(test,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(test,serializer.validated_data)
        return Response(serializer.data)

    def partial_update(self,request,name):
        test = get_object_or_404(self.queryset,name=name)
        serializer = TestSerializer(test,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(test,serializer.validated_data)
        return Response(serializer.data)
    
    def destroy(self,rquest,name):
        test = get_object_or_404(self.queryset,name=name)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
