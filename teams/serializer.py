from teams.models import Teams
from rest_framework import serializers
from common.serializer import ProfileSerializer


class TeamsSerializer(serializers.ModelSerializer):
    users = ProfileSerializer(read_only=True, many=True)
    created_by = ProfileSerializer()

    class Meta:
        model = Teams
        fields = (
            "id",
            "name",
            "description",
            "users",
            "created_on",
            "created_by",
            "created_on_arrow",
        )


class TeamCreateSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        request_obj = kwargs.pop("request_obj", None)
        super(TeamCreateSerializer, self).__init__(*args, **kwargs)
        self.org = request_obj.org

        self.fields["name"].required = True

    def validate_name(self, name):
        if self.instance:
            if (
                Teams.objects.filter(
                    name__iexact=name, org=self.org
                )
                .exclude(id=self.instance.id)
                .exists()
            ):
                raise serializers.ValidationError("Team already exists with this name")
        else:
            if Teams.objects.filter(name__iexact=name).exists():
                raise serializers.ValidationError("Team already exists with this name")
        return name

    class Meta:
        model = Teams
        fields = (
            "name",
            "description",
            "created_on",
            "created_by",
            "created_on_arrow",
            "org"
        )
