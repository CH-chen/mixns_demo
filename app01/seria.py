
from app01 import models
from rest_framework import serializers

class PublisherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = "__all__"

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"

        # 以上是默认的
        # 显示超链接
    publisher = serializers.HyperlinkedIdentityField(
        view_name="publisher_detail",  # url中的别名
        lookup_field="publisher_id", #关联字段的字段名
        lookup_url_kwarg="pk",
    )
    # 默认一对多，多对多显示主键，可以自定义显示字段为name和其他字段， 可以不加就显示全部  publisher用自定义的话post请求要重写create方法
    # publisher = serializers.CharField(source="publisher.name",read_only=True)#一对多可以用 自定义字段
    # authors = serializers.CharField(source="authors.all") #多对多不好用
    # 多对多自定义显示字段用下面这个，默认显示主键
    # authors =serializers.SerializerMethodField() 自定义字段
    # def get_authors(self,obj):
    #     temp = []
    #     for obj in obj.authors.all():
    #         temp.append(obj.name)
    #         print(temp)
    #     return temp
    # 自定义显示字段 用自定义的话post请求要重写create方法,不自定义用默认的就不需要create方法
    # def create(self,validated_data):
    #     print("validated_data",validated_data)
    #     book = models.Book.objects.create(title=validated_data["title"],price=validated_data["price"],pub_date=validated_data["pub_date"],publisher_id=validated_data["publisher"].split("/")[-2])
    #     book.authors.add(*validated_data["authors"])
    #     return book

class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"
