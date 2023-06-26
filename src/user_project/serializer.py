from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import *


class JoinUserProjectSerializer(serializers.ModelSerializer):
    account_discord = serializers.CharField(
        max_length=25,
        validators=[RegexValidator(r'^\w+#\d{4}$', 'Invalid Discord username format')]
    )
    conditions_participation = serializers.BooleanField(default=True)
    processing_personal_data = serializers.BooleanField(default=True)

    def create(self, validated_data):
        conditions_participation = validated_data.get('conditions_participation')
        processing_personal_data = validated_data.get('processing_personal_data')
        if conditions_participation is not True and processing_personal_data is not True:
            raise serializers.ValidationError("Field 'conditions_participation' must be set to True.")
        return super().create(validated_data)

    class Meta:
        model = JoinProject
        fields = '__all__'
