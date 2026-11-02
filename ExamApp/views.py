from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ExamApp.models import QuestionDb,AnswerDb
from ExamApp.serializers import QuestionSerializer,AnswerSerializer

# Create your views here.
class QuestionListCreateView(APIView):
    def get(Self,request):
        qs=QuestionDb.objects.all()

        serializer_instance=QuestionSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            orginal_data=serializer_instance.validated_data
            QuestionDb.objects.create(**orginal_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class QuestionRetrieveUpdateDelete(APIView):
    def get(self,request,pk):

        qs=QuestionDb.objects.get(id=pk)

        serializer_instance=QuestionSerializer(qs)

        return Response(data=serializer_instance.data)
      

    def put(self,request,pk):
        form_data=request.data

        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():

            actual_data=serializer_instance.validated_data

            QuestionDb.objects.filter(id=pk).update(**actual_data)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        QuestionDb.objects.filter(id=pk).delete()

        return Response(
            {"message":"Question Deleted successfully"}
        )



class answerListView(APIView):
    def get(self,request):
        ans=AnswerDb.objects.all()
        serializer_instance=AnswerSerializer(ans,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=AnswerSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            AnswerDb.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)