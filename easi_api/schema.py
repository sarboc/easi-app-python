import graphene
from graphene_django import DjangoObjectType

from easi_api.easi_api.models import AccessibilityRequest, AccessibilityTestDate, System

class SystemType(DjangoObjectType):
    class Meta:
        model = System
        fields = ("id", "name", "lcid")

class DateType(DjangoObjectType):
    class Meta:
        model = AccessibilityTestDate
        fields = ("id", "date", "score")

class AccessibilityRequestType(DjangoObjectType):
    class Meta:
        model = AccessibilityRequest
        fields = ("id", "name", "system", "dates")

class Query(graphene.ObjectType):
    all_systems = graphene.List(SystemType)
    all_accessibility_requests = graphene.List(AccessibilityRequestType)
    all_test_dates = graphene.List(DateType)

    def resolve_all_systems(root, info):
        return System.objects.all()
    
    def resolve_all_accessibility_requests(root, info):
        return AccessibilityRequest.objects.all()

    def resolve_all_test_dates(root, info):
        return AccessibilityTestDate.objects.all()

schema = graphene.Schema(query=Query)