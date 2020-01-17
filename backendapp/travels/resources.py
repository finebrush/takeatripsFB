
from model_import_export.resources import ModelResource, ForeignKeyResource, ManyToManyResource, RelatedResource

# from import_export import resources
from .models import InfoTravel

class SubjectResource(ModelResource):
    city = ForeignKeyResource(column='nameko')
    categorylarge = ForeignKeyResource(column='name')
    categorymedium = ForeignKeyResource(column='name')
    categorysmall = ForeignKeyResource(column='name')
    tagko = ForeignKeyResource(column='name')
    tageng = ForeignKeyResource(column='name')
    tagven = ForeignKeyResource(column='name')
    like_infotravel = ManyToManyResource(column='user')
    likeits = RelatedResource(column='user')

    class Meta:
        model = InfoTravel
        fields = ['city', 'companyko', 'companyeng', 'companyven', 'picture1', 'picture2', 'picture3', 'picture4', 'picture5',
            'picture6', 'picture7', 'picture8', 'picture9', 'picture10', 'asset', 'part' , 'typeit', 'addressko', 'addresseng',
            'addressven', 'categorylarge', 'categorymedium', 'categorysmall', 'linkweb', 'linkinsta', 'linkyoutube', 'trafficko',
            'trafficeng', 'trafficven', 'introko', 'introeng', 'introven', 'itdate', 'itlocation', 'like_infotravel', 'tagko', 'tageng', 'tagven',]
        # fields = '__all__'
        # exclude = ['city', 'categorylarge', 'categorymedium', 'categorysmall', 'tagko', 'tageng', 'tagven', 'like_infotravel']