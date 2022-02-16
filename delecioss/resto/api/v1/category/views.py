from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api.v1.category.serializer import CategorySerializer
from api.v1.category.services import cat_one, cat_list
from recipe.models import Category


class CategoryView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            root = Category.objects.get(pk=pk)
        except:
            raise NotFound('Category object not found')

        return root

    def get(self, requests, *args, **kwargs):
        if 'pk' in kwargs and kwargs['pk']:
            result = cat_one(kwargs['pk'])
        else:
            result = cat_list(requests)

        return Response(result, status=HTTP_200_OK)

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        root = serializer.create(serializer.data)
        result = cat_one(root.pk)
        return Response(result, status=HTTP_200_OK)

    def put(self, requests, *args, **kwargs):
        root = self.get_object(kwargs['pk'])
        serializer = self.get_serializer(data=requests.data, instance=root)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        result = cat_one(root.pk)
        return Response(result, status=HTTP_200_OK)

    def delete(self, requests, *args, **kwargs):
        self.get_object(kwargs['pk']).delete()
        return Response({"success": "bu narsa o`chirildi"}, status=HTTP_200_OK)
















