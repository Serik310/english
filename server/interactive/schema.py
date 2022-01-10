import graphene
from graphene_django import DjangoObjectType

from .models import Word


class WordType(DjangoObjectType):
    class Meta:
        model = Word
        fields = ('id', 'name', 'transcription', 'description')


class Query(graphene.ObjectType):
    all_words = graphene.List(WordType)

schema = graphene.Schema(query=Query)
