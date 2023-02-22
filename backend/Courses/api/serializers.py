from .models import Course, Lesson, Custom_user
from rest_framework import serializers
    
class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_user
        fields = ['id', 'username']

class UserSerializer(serializers.ModelSerializer):
    friends = SimpleUserSerializer(many=True, read_only=True)
    class Meta:
        model = Custom_user
        fields = ['id', 'username', 'friends']
        depth = 1

class UserAddFriendSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class UserLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'course']
        depth = 1

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description']

class LessonSerializer(serializers.ModelSerializer):
    taken_by = SimpleUserSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'course', 'taken_by']
        depth = 1

class LessonAddUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

class FriendshipSerializer(serializers.Serializer):
    friendships = serializers.ListField(
        child=SimpleUserSerializer(many=True))

__all__ = ['UserSerializer', 'CourseSerializer', 'LessonSerializer', 'UserAddFriendSerializer', 
           'LessonAddUserSerializer', 'UserLessonsSerializer', 'SimpleUserSerializer', 'FriendshipSerializer']