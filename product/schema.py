import graphene
from graphene_django import DjangoObjectType

from product.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("name", "slug")


class TestProductType(ProductType):
    class Meta:
        model = Product
        fields = ("description",)


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    testproducts = graphene.List(TestProductType)
    product = graphene.Field(ProductType, pk=graphene.Int())

    @staticmethod
    def resolve_product(root, info, **kwargs):
        pk = kwargs.get('pk')

        if pk is not None:
            return Product.objects.get(pk=pk)

        return None

    def resolve_products(root, info, **kwargs):
        return Product.objects.all()

    def resolve_testproducts(root, info, **kwargs):
        return Product.objects.all()


schema = graphene.Schema(query=Query)
