from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from decimal import Decimal


class ItemsMixin:
    @property
    def data(self):
        return [
            {"id": 1, "name": "olive oil", "price": Decimal("8.99")},
            {"id": 2, "name": "flour", "price": Decimal("3.50")},
            {"id": 3, "name": "salt", "price": Decimal("2.50")},
            {"id": 4, "name": "yeast", "price": Decimal("1.50")},
            {"id": 5, "name": "whole canned tomatoes", "price": Decimal("4.50")},
        ]


class UserMixin:
    @property
    def data(self):
        return [
            {"id": 1, "name": "Bill", "store_credits": Decimal("10")},
            {"id": 2, "name": "Bob", "store_credits": Decimal("60")},
            {"id": 3, "name": "Jim", "store_credits": Decimal("30.50")},
            {"id": 4, "name": "Jack", "store_credits": Decimal("34.80")},
            {"id": 5, "name": "Mona", "store_credits": Decimal("18")},
        ]


class ItemListView(APIView, ItemsMixin):

    def get(self, request, format=None):
        return Response(self.data, status=status.HTTP_200_OK)


class ItemDetailView(APIView, ItemsMixin):

    def get(self, request, pk, format=None):
        from pprint import pprint
        if pk <= len(self.data) and pk > 0:
            return Response(self.data[pk - 1], status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class UserListView(APIView, UserMixin):
    def get(self, request, format=None):
        return Response(self.data, status=status.HTTP_200_OK)


class UserDetailView(APIView, UserMixin):
    def get(self, request, pk, format=None):
        if pk <= len(self.data) and pk > 0:
            return Response(self.data[pk - 1], status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
