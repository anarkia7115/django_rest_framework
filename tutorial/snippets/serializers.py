#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
  snippets = serializers.HyperlinkedIndentityField(
    many=True,
    view_name='snippet-detail', 
    read_only=True
  )

  class Meta:
    model = User
    fields = ('id', 'username', 'snippets')



class SnippetSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.ReadOnlyField( source='owner.username' )
  highlight = serializers.HyperlinkedIndentityField(
    view_name='snippet-highlight', 
    format='html'
  )

  class Meta:
    model = Snippet
    fields = ('url', 'owner', 'id', 'title', 
              'code', 'linenos', 'language', 'style')
