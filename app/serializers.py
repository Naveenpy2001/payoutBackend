from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone_number', 'resume')

class ResumeHeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['resume_headline']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'phone_number', 'resume')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number'),
            resume=validated_data.get('resume'),
        )
        return user


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

User = get_user_model()

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)

            if not user:
                raise serializers.ValidationError("Invalid email or password")
        else:
            raise serializers.ValidationError("Must include email and password")

        data = super().validate(attrs)
        data['user'] = UserSerializer(user).data
        return data


# update resume

class ResumeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('resume',)