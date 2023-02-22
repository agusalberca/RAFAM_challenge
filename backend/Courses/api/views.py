from .models import Course, Lesson, Custom_user
from . import serializers
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response

class Custom_userViewSet(viewsets.ModelViewSet):
    queryset = Custom_user.objects.all()
    serializer_class = serializers.UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        '''Creates a new user'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def add_friend(self, request, pk=None):
        '''Adds a friend to the user'''
        user = self.get_object()
        serializer = serializers.UserAddFriendSerializer(data=request.data)
        if serializer.is_valid():
            try:
                friend = Custom_user.objects.get(pk=serializer.data['id'])
            except Custom_user.DoesNotExist:
                return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user.friends.add(friend)
        user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data)        
    
    @action(detail=True, methods=['get'])
    def friends(self, request, pk=None):
        '''Returns the friends of the user'''
        user = self.get_object()
        friends = user.friends.all()
        serializer = serializers.SimpleUserSerializer(friends, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def lessons(self, request, pk=None):
        '''Returns the lessons of the user'''
        user = self.get_object()
        lessons = Lesson.objects.filter(taken_by=user)
        serializer = serializers.UserLessonsSerializer(lessons, many=True)
        return Response(serializer.data)
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        '''Creates a new course'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        '''Creates a new lesson'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def add_user(self, request, pk=None):
        '''Adds a user to the lesson'''
        lesson = self.get_object()
        serializer = serializers.LessonAddUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = Custom_user.objects.get(pk=serializer.data['user_id'])
            except Custom_user.DoesNotExist:
                return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        lesson.taken_by.add(user)
        lesson.save()
        serializer = self.serializer_class(lesson)
        return Response(serializer.data)

class FriendshipViewSet(viewsets.ViewSet):
    queryset = Custom_user.objects.all()

    def list(self, request):
        '''Returns a list of all friendships
        Format: list of lists of two users'''
        friendships = []
        friend_set = set()
        users = Custom_user.objects.all()
        for user in users:
            friends = user.friends.all()
            for friend in friends:
                if (user.id, friend.id) not in friend_set and (friend.id, user.id) not in friend_set:
                    friend_set.add((user.id, friend.id))
                    friendships.append([
                        {"id": user.id, "username": user.username},
                        {"id": friend.id, "username": friend.username}
                    ])
        serializer = serializers.FriendshipSerializer({"friendships" :friendships})
        return Response(serializer.data['friendships'])