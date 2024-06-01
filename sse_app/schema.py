import graphene
from graphene_django import DjangoObjectType
from sse_app.models import MyModel

class MyModelType(DjangoObjectType):
    class Meta:
        model = MyModel

class Query(graphene.ObjectType):
    all_models = graphene.List(MyModelType)

    def resolve_all_models(self, info):
        return MyModel.objects.all()

class CreateMyModel(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    my_model = graphene.Field(MyModelType)

    def mutate(self, info, name, description):
        my_model = MyModel(name=name, description=description)
        my_model.save()
        return CreateMyModel(my_model=my_model)

class Mutation(graphene.ObjectType):
    create_my_model = CreateMyModel.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
