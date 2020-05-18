from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from ..models import Snippet
from ..serializers import SnippetSerializer


def run():
    snippet = Snippet(code='foo = "bar"\n')
    snippet.save()

    snippet = Snippet(code='print("hello, world")\n')
    snippet.save()
