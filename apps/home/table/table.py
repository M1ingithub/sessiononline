import django_tables2 as tables
from apps.home.models.communitymodel import CommunityModel

class CommunityTable(tables.Table):
    id = tables.Column()
    age = tables.Column()
    class Meta:
        model = CommunityModel
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )
        attrs = {"class": "mytable"}

table = CommunityTable('asd')
