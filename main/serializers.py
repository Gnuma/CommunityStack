from rest_framework import serializers
from .models import Category, Topic, Tutorial
from .user_management.utils import _userExist, _createUser, _getUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Topic


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Tutorial


class ContributeSerializer(serializers.Serializer):
    link = serializers.URLField(required = True)
    email = serializers.EmailField(required = True)
    username = serializers.CharField(min_length = 3, max_length = 255, required = True)
    topic = serializers.IntegerField(required = True)

    def validate_topic(self, topic):
        try:
            Topic.objects.get(pk = topic)
        except Topic.DoesNotExist:
            raise serializers.ValidationError(
                'The topic does not exist!'
            )
        
        return topic

    def validate(self, data):
        if  not _userExist(data['email'], data['username']):
            data['user'] = _createUser(data['email'], data['username'])
        else:
            data['user'] = _getUser(data['email'], data['username'])
        return data 

    def save(self):
        data = self.validated_data

        topic = Topic.objects.get(pk = data['topic'])

        newTutorial = Tutorial.objects.create(
            link = data['link'],
            user = data['user'],
            topic = topic
            )

        newTutorial.save()
        
        return 1