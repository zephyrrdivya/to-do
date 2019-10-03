from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.deadline_date = validated_data.get(
            'deadline_date', instance.deadline_date)
        instance.isCompleted = validated_data.get(
            'isCompleted', instance.isCompleted)
        instance.save()
        return instance

    class Meta:
        model = Task
        fields = ('url', 'id', 'title', 'content',
                  'deadline_date', 'isCompleted', 'user')
