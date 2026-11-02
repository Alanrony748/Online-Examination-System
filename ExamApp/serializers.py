from rest_framework import serializers
from ExamApp.models import QuestionDb,AnswerDb

class QuestionSerializer(serializers.Serializer):
    question=serializers.CharField(max_length=500)
    option_a=serializers.CharField(max_length=500)
    option_b=serializers.CharField(max_length=500)
    option_c=serializers.CharField(max_length=500)
    option_d=serializers.CharField(max_length=500)
    correct_answer=serializers.CharField(max_length=500)


class AnswerSerializer(serializers.Serializer):
    answer=serializers.CharField()
    question_id=serializers.IntegerField()
    points=serializers.IntegerField(read_only=True)
    owner=serializers.CharField()
    submission_date=serializers.DateTimeField(read_only=True)
    remarks=serializers.CharField(read_only=True)


    def validate(self,validated_data):
        question_id=validated_data.get("question_id")
        if not QuestionDb.objects.filter(id=question_id).exists():
            raise serializers.ValidationError
        return validated_data