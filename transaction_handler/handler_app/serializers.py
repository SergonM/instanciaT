from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    curso_id = serializers.IntegerField(required=False)
    nombre = serializers.CharField(max_length=100)
    descripcion = serializers.CharField()
    accion = serializers.ChoiceField(choices=['crear', 'actualizar'])
