
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404



class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        print("posting")
        username = data['username']
        name = data['name']
        age = data['age']
        sex = data['sex']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return Response({'error': 'أسم المستخدم مستعمل من قبل'})
            else:
                if len(password) < 6:
                    return Response({'error': 'كلمه السر يجب الاتقل عن 6 عناصر'})
                else:
                    user = User.objects.create_user(username=username, name=name, age = age, sex = sex,  password=password)

                    user.save()
                    return Response({'success': 'تم تسجيل مستخدم جديد'})
        else:
            return Response({'error': 'كلمة السر ليست متطابقة'})


class GetAllUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(instance=users, many = True)
        return Response(serializer.data)


class DeleteUser(APIView):
    def delete(self, request, id):
        user = User.objects.filter(id = id)
        if user.exists():
            user.delete()
            return Response({"message":"تم حذف اسم المستخدم"})
        else:
            return Response({"message":"المستخدم ليس متاح"})

        