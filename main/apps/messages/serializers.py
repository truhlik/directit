from rest_framework import serializers

from .models import Message, MessageThread
from .utils import can_write_to_thread
from ..users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    thread_ct_id = serializers.IntegerField(source='thread.object_id')
    replies = serializers.IntegerField(read_only=True)

    class Meta:
        model = Message
        fields = [
            'id',
            'owner',
            'thread_ct_id',
            'text',
            'parent',
            'created_at',
            'updated_at',
            'replies',
        ]

    def validate_thread_ct_id(self, thread_ct_id):
        try:
            thread = MessageThread.objects.get(object_id=thread_ct_id)
        except MessageThread.DoesNotExist:
            raise serializers.ValidationError('neplatné thread id')

        if self.instance is not None and thread != self.instance.thread:
            raise serializers.ValidationError('nemůžete změnit vlákno')

        if not can_write_to_thread(thread.content_object, self.context['request'].user):
            raise serializers.ValidationError('nemáte oprávnění psát do tohoto thread id')

        return thread

    def validate_parent(self, parent):
        if self.instance is not None and parent != self.instance.parent:
            raise serializers.ValidationError('nemůžete změnit nadřazenou zprávu')
        return parent

    def validate(self, attrs):
        thread = attrs.get("thread")["object_id"]
        parent = attrs.get("parent")
        if parent and parent.thread != thread:
            raise serializers.ValidationError({
                'thread': "parent nema stejne vlakno",
                'parent': "parent nema stejne vlakno",
            })
        return attrs

    def save(self, **kwargs):
        self.validated_data['thread'] = self.validated_data.pop("thread")["object_id"]
        self.validated_data['owner'] = self.context['request'].user
        return super(MessageSerializer, self).save(**kwargs)
