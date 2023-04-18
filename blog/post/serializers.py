from rest_framework.serializers import ModelSerializer
from .models import Post
from review.serializers import CommentSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        # rep['likes'] = Like.objects.filter(post=instance)
        # rep['test'] = 'hello'
        # print(rep)

        rep['likes'] = instance.likes.all().count()

        comments = instance.comments.all() # все комменты данного поста
        rep['comments'] = CommentSerializer(comments, many=True).data
        # rep['aaaaa'] = {'a':1} # пример отображения, representation

        return rep
    
    #  попробуйте написать модель комментарий, для начала как с постами (listing)
    # на создание, на листинг, на удаление
    # доп    вьюшки  (@api_view)












    
