from pickle import TRUE
from xml.dom import ValidationErr
from rest_framework import serializers

from .models import Section

class SubSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('title', 'body', 'last_updated')


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ['id','created_at','last_updated', 'title', 'body','parent_section']
        depth = 2
    
    def create(self, validated_data):
        return Section.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
    
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.parent_section = validated_data.get('parent_section', instance.parent_section)
        instance.last_updated = validated_data.get('last_updated', instance.last_updated)
        instance.save()
        
        return instance

    # def to_representation(self, instance):
    #     self.fields['parent_section'] = SectionSerializer(read_only=True)
    #     return super(SectionSerializer, self).to_representation(instance)