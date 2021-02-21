import graphene
from graphene_django import DjangoObjectType

from easi_api.systems.models import System

class SystemType(DjangoObjectType):
    class Meta:
        model = System
        fields = ("id", "name", "lcid")

class Query(graphene.ObjectType):
    all_systems = graphene.List(SystemType)

    def resolve_all_systems(root, info):
        return System.objects.all()

schema = graphene.Schema(query=Query)