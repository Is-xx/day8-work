from rest_framework.response import Response
from rest_framework.views import APIView

from test_app.models import Teacher
from test_app.serializers import TeacherSerializer
from test_app.serializers import TeacherDeSeralizer


class TeacherAPIView(APIView):

    def get(self, resquest, *args, **kwargs):
        id = kwargs.get('id')
        if id:
            obj = Teacher.objects.get(pk=id)
            teacher = TeacherSerializer(obj).data
            return Response({
                'status': 200,
                'message': '查询单个教师成功',
                'results': teacher
            })
        else:
            obj = Teacher.objects.all()
            teachers = TeacherSerializer(obj, many=True).data
            return Response({
                'status': 200,
                'message': '查询所有教师成功',
                'results': teachers
            })

    def post(self, resquest, *args, **kwargs):
        data = resquest.data
        if not isinstance(data, dict) or data == {}:
            return Response({
                "status": 400,
                "message": "参数有误",
            })
        serializer = TeacherDeSeralizer(data=data)
        if serializer.is_valid():
            teacher = serializer.save()
            return Response({
                "status": 200,
                "message": "员工添加成功",
                "results": TeacherSerializer(teacher).data
            })
        else:
            return Response({
                "status": 400,
                "message": "员工添加失败",
                "results": serializer.errors
            })
