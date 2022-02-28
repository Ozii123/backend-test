from pickle import TRUE
from xml.dom import ValidationErr
from rest_framework import serializers

from .models import Section

class SubSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('title', 'body', 'last_updated')


class SectionSerializer(serializers.ModelSerializer):
    # # title = serializers.CharField(max_length=20000)
    # # body = serializers.CharField(max_length=20000000)
    # # last_updated = serializers.DateTimeField(required=False)
    # parent_section = serializers.SerializerMethodField()

    # def get_parent_section(self, obj):
    #     if obj.parent_section is not None:
    #         return SectionSerializer(obj.parent_section).data
    class Meta:
        model = Section
        fields = ['id','created_at','last_updated', 'title', 'body','parent_section']
        depth = 2
    def create(self, validated_data):
        return Section.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.parent_section = validated_data.get('parent_section', instance.parent_section)
        instance.last_updated = validated_data.get('last_updated', instance.last_updated)
        instance.save()
        
        return instance

    # def to_representation(self, instance):
    #     self.fields['parent_section'] = SectionSerializer(read_only=True)
    #     return super(SectionSerializer, self).to_representation(instance)