from django.shortcuts import render
from app01 import models
from app01 import seria

from rest_framework import mixins
from rest_framework import generics

#*********第一种继承方法
class PublsherMixView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):

    queryset = models.Publisher.objects.all()
    serializer_class = seria.PublisherModelSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class PublisherDetailMix(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):

    queryset = models.Publisher.objects.all()
    serializer_class = seria.PublisherModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class BookMixView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):

    queryset = models.Book.objects.all()
    serializer_class = seria.BookModelSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        print("=======")
        print(request.data)
        return self.create(request,request.data,*args,**kwargs)

class BookDetailMix(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):

    queryset = models.Book.objects.all()
    serializer_class = seria.BookModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("$$$$$$$")
        print(request.data)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

##***************第二种继承方法

from app01 import seria2
from rest_framework import mixins
from rest_framework import generics

class PublsherGenView(generics.ListCreateAPIView):

    queryset = models.Publisher.objects.all()
    serializer_class = seria2.PublisherModelSerializer

class PublisherDetailGen(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Publisher.objects.all()
    serializer_class = seria2.PublisherModelSerializer

class BookGenView(generics.ListCreateAPIView):

    queryset = models.Book.objects.all()
    serializer_class = seria2.BookModelSerializer

class BookDetailGen(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Book.objects.all()
    serializer_class = seria2.BookModelSerializer


#####*********第三种**
from rest_framework import viewsets
class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = seria2.BookModelSerializer