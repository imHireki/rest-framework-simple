from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html'
    )

    class Meta:
        model = Snippet
        """
        Our snippet and user serializers include 'url' fields
        that by default will refer to '{model_name}-detail',
        which in this case will be 'snippet-detail' and 'user-detail'.
        """
        fields = [
            'url', 'id', 'highlight', 'owner', 'title',
            'code', 'linenos', 'language', 'style'
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='snippet-detail',
        read_only=True
    )

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
