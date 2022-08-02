from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class DonateurMSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DonateurUser
        fields=['user_name','last_name','email','numero','password']
        extra_kwargs ={
            'password':{'write_only':True}
        }
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance =self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class DonateurOrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DonateurUser
        fields=['user_name','last_name','email','numero','organisations','password']
        extra_kwargs ={
            'password':{'write_only':True}
        }
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance =self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EffectuerArgSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectuerDonArge
        fields = ["id","donateur","typeDons","categorieV","cibleV","montant","provider","affecter"]

class EffectuerNatSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectuerDonNature
        fields = ["id","donateur","typeDons","categorieV","cibleV","categorieObjet","typeObjet","lieu_reception","Etat","photo","affecter"]


# class ESerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EffectuerDon
#         fields = ["id","donateur","typeDons","categorieV","cibleV","categorieObjet","typeObjet","lieu_reception","Etat","photo","affecter","montant","provider"]