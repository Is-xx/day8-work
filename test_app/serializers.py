from django.conf import settings
from rest_framework import serializers

from test_app.models import Teacher


class TeacherSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    age = serializers.IntegerField()
    phone = serializers.CharField()
    gender = serializers.SerializerMethodField()
    pic = serializers.SerializerMethodField()

    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_pic(self, obj):
        return '%s%s%s' % ("http://127.0.0.1:8000/", settings.MEDIA_URL, str(obj.pic))


class TeacherDeSeralizer(serializers.Serializer):
    username = serializers.CharField(
        max_length=4,
        min_length=2,
        error_messages={
            'max_length': '姓名长度超出范围',
            'min_length': '姓名字数不够',
        }
    )
    password = serializers.CharField()
    phone = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.IntegerField()
    pic = serializers.ImageField()

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
