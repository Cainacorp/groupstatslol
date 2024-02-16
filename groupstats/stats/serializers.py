from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import *

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        depth = 1


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
        depth = 1


class UserSerializer(ModelSerializer):
    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)

    class Meta:
        model = get_user_model()
        # fields = ('pk', 'username', 'email', 'first_name', 'last_name')
        # read_only_fields = ('email', )
        fields = '__all__'


class UserSerializerBasic(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'first_name', 'last_name')


class SummonerSerializer(ModelSerializer):

    kda = ReadOnlyField()
    log_scraping_name = ReadOnlyField()
    complete_name = ReadOnlyField()

    class Meta:
        model = Summoner
        fields = '__all__'

class SummonerGroupSerializer(ModelSerializer):
    class SummonerSerializerOut(ModelSerializer):
        
        complete_name = ReadOnlyField()

        class Meta:
            model = Summoner
            fields = ['id', 'complete_name']

        def to_representation(self, instance):
            response = super().to_representation(instance)
            response['summoners'] = self.SummonerSerializerOut(instance.summoner, many=True, read_only=True).data
            return response

class RoleSerializer(ModelSerializer):

    class SummonerSerializerOut(ModelSerializer):
        
        complete_name = ReadOnlyField()

        class Meta:
            model = Summoner
            fields = ['id', 'complete_name']
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['summoner'] = self.SummonerSerializerOut(instance.summoner, read_only=True).data
        return response
    
    class Meta:
        model = Role
        fields = '__all__'
    

class PlayWithSerializer(ModelSerializer):

    class SummonerSerializerOut(ModelSerializer):
        
        complete_name = ReadOnlyField()

        class Meta:
            model = Summoner
            fields = ['id', 'complete_name']
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['summoner'] = self.SummonerSerializerOut(instance.summoner, read_only=True).data
        response['played_with'] = self.SummonerSerializerOut(instance.played_with, read_only=True).data
        return response
    
    class Meta:
        model = PlayWith
        fields = '__all__'


        
