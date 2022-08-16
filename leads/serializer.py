from rest_framework import serializers
from leads.models import Lead, Company
from accounts.models import Tags, Account
from common.serializer import (
    ProfileSerializer,
    AttachmentsSerializer,
    LeadCommentSerializer,
    OrganizationSerializer
)
from teams.serializer import TeamsSerializer
from contacts.serializer import ContactSerializer


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ("id", "name", "slug")


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "name")


class LeadSerializer(serializers.ModelSerializer):
    contacts=ContactSerializer(read_only=True, many=True)
    assigned_to = ProfileSerializer(read_only=True, many=True)
    created_by = ProfileSerializer()
    country = serializers.SerializerMethodField()
    tags = TagsSerializer(read_only=True, many=True)
    lead_attachment = AttachmentsSerializer(read_only=True, many=True)
    teams = TeamsSerializer(read_only=True, many=True)
    lead_comments = LeadCommentSerializer(read_only=True, many=True)
    

    def get_country(self, obj):
        return obj.get_country_display()

    class Meta:
        model = Lead
        # fields = ‘__all__’
        fields = (
            "id",
            "title",
            "first_name",
            "last_name",
            "phone",
            "email",
            "status",
            "source",
            "address_line",
            "contacts",
            "street",
            "city",
            "state",
            "postcode",
            "country",
            "website",
            "description",
            "lead_attachment",
            "lead_comments",
            "assigned_to",
            "account_name",
            "opportunity_amount",
            "created_by",
            "created_on",
            "is_active",
            "enquiry_type",
            "tags",
            "created_from_site",
            "teams",
            "skype_ID",
            "industry",
            "company",
            "organization",
            "probability",
            "close_date"
        )


class LeadCreateSerializer(serializers.ModelSerializer):
    probability = serializers.IntegerField(max_value=100)
    def __init__(self, *args, **kwargs):
        request_obj = kwargs.pop("request_obj", None)
        super().__init__(*args, **kwargs)
        if self.initial_data.get("status") == "converted":
            self.fields["account_name"].required = True
            self.fields["email"].required = True
        self.fields["first_name"].required = False
        self.fields["last_name"].required = False
        self.fields["title"].required = True
        self.org = request_obj.org

        if self.instance:
            if self.instance.created_from_site:
                prev_choices = self.fields["source"]._get_choices()
                prev_choices = prev_choices + \
                    [("micropyramid", "Micropyramid")]
                self.fields["source"]._set_choices(prev_choices)

    def validate_account_name(self, account_name):
        if self.instance:
            if (
                Account.objects.filter(
                    name__iexact=account_name,
                    org=self.org
                )
                .exclude(id=self.instance.id)
                .exists()
            ):
                raise serializers.ValidationError(
                    "Account already exists with this name"
                )
        else:
            if Account.objects.filter(
                name__iexact=account_name,
                org=self.org
            ).exists():
                raise serializers.ValidationError(
                    "Account already exists with this name"
                )
        return account_name

    def validate_title(self, title):
        if self.instance:
            if (
                Lead.objects.filter(
                    title__iexact=title,
                    org=self.org
                )
                .exclude(id=self.instance.id)
                .exists()
            ):
                raise serializers.ValidationError(
                    "Lead already exists with this title")
        else:
            if Lead.objects.filter(title__iexact=title, org=self.org).exists():
                raise serializers.ValidationError(
                    "Lead already exists with this title")
        return title

    class Meta:
        model = Lead
        fields = (
            "first_name",
            "last_name",
            "account_name",
            "title",
            "phone",
            "email",
            "status",
            "source",
            "website",
            "description",
            "address_line",
            #"contacts",
            "street",
            "city",
            "state",
            "postcode",
            "opportunity_amount",
            "country",
            "org",
            "skype_ID",
            "industry",
            "company",
            "organization",
            "probability",
            "close_date",
            #"lead_attachment",
        )
