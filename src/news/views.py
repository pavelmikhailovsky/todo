from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NewsSerializer

from .models import News


@api_view(['GET'])
def news_list(request):
    """ Вывод всех новостей """
    news = News.objects.order_by('-create_at')
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)    

        
