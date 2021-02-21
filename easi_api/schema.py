import graphene
from graphene_django import DjangoObjectType

from easi_api.systems.models import AccessibilityRequest, System

class SystemType(DjangoObjectType):
    class Meta:
        model = System
        fields = ("id", "name", "lcid")

class AccessibilityRequestType(DjangoObjectType):
    class Meta:
        model = AccessibilityRequest
        fields = ("id", "name", "system")

class Query(graphene.ObjectType):
    all_systems = graphene.List(SystemType)
    all_accessibility_requests = graphene.List(AccessibilityRequestType)

    def resolve_all_systems(root, info):
        return System.objects.all()
    
    def resolve_all_accessiblity_requests(root, info):
        return AccessibilityRequest.objects.all()

schema = graphene.Schema(query=Query)