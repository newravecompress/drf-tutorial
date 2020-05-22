from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

User = get_user_model()


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']
