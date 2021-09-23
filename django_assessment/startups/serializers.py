from django_assessment.startups.models import Country, Stage, Startup
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ['stage_name']
    
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name','country_code']

class StartupSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    stage = StageSerializer(read_only=True)
    class Meta:
        model = Startup
        fields = ['startup_name','website','one_liner','description','city','founded','money_raised_usd','country','stage','created','updated']
