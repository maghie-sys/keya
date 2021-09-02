from rest_framework import serializers
from .models import Er, ErAd, Th, ThGr, ThPic
from django.db.models import Avg, Max, Min, Sum, Count

class home_recom_serializer(serializers.ModelSerializer):
    class Meta:
        model = Th
        fields = (
            'Th_CODE',
            'Th_Name',
            'Th_Genre',
            'Th_Pic1'
        )

class sh_th_gr_serializer(serializers.ModelSerializer):
    class Meta:
        model = ThGr
        fields = (
            'ThGr_pt',
            'ThGr_review'
        )

class ThpicSerializer(serializers.ModelSerializer):
    Th_pic = serializers.ImageField(use_url=True)
    class Meta:
        model = ThPic
        fields = ('Th_pic')

class sh_th_serializer(serializers.ModelSerializer):
    ThGr_avpt = serializers.SerializerMethodField()
    ThGr_pt = serializers.SerializerMethodField()
    ThGr_review = serializers.SerializerMethodField()
    Th_pics = serializers.SerializerMethodField()
    Th_pics = ThpicSerializer(many=True, read_only=True)

    class Meta:
        model = Th
        fields = (
            'Th_Name',
            'Th_Genre',
            'Th_Diff',
            'Th_Fear',
            'Th_Act',
            'Th_Intro',
            'ThGr_avpt',
            'ThGr_pt',
            'ThGr_review',
            'Th_pics'
        )
    def get_ThGr_avpt(self, obj):
        return ThGr.objects.aggregate(Avg('ThGr_pt'))

    def get_ThGr_pt(self, obj):
        return ThGr.objects.all().order_by('-ThGr_pt').values('ThGr_pt').first()

    def get_ThGr_review(self, obj):
        return ThGr.objects.all().order_by('-ThGr_pt').values('ThGr_review').first()

    def create(self, validated_data):
        instance = Th.objects.create(**validated_data)
        Th_pic_set = self.context['request'].FILES
        for image_data in Th_pic_set.getlist('Th_pic'):
            ThPic.objects.create(th=instance, Th_pic=image_data)
        return instance

    '''
        def get_Th_pics(self, obj):
            Th_pic = obj.Th_pic_set.all()
            return ThpicSerializer(instance=Th_pic, many=True).data
    '''



