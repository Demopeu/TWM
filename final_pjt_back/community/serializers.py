from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'username']

    user = UserSerializer(read_only=True)
    new_created_at = serializers.SerializerMethodField()
    new_updated_at = serializers.SerializerMethodField()
    like_users_count = serializers.IntegerField(source='likes_users.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
    
    def get_new_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d")
    
    def get_new_updated_at(self, obj):
        return obj.updated_at.strftime("%Y-%m-%d")


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'country']



class ArticleSerializer(serializers.ModelSerializer):

    class CommentDetailSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['username']
        user = UserSerializer(read_only=True)
        class Meta:
            model = Comment
            fields = '__all__'

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ['id', 'username']

    user = UserSerializer(read_only=True)
    comment_set = CommentDetailSerializer(read_only=True, many=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_users_count = serializers.IntegerField(source='likes_users.count', read_only=True)
    new_created_at = serializers.SerializerMethodField()
    new_updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
    
    def get_new_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d")
    
    def get_new_updated_at(self, obj):
        return obj.updated_at.strftime("%Y-%m-%d")


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'username']

    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['user', 'content']
    
    def create(self, validated_data):
        # 현재 요청을 보낸 사용자를 작성자로 설정
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
