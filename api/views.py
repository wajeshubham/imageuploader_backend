from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import generics

from .models import UploadedImage
from .serializers import UploadedImageSerializer


# Create your views here.

class ImageView(generics.ListAPIView):
    queryset = UploadedImage.objects.all().order_by("-date")
    serializer_class = UploadedImageSerializer


@api_view(['POST'])
def upload_img(request):
    img = UploadedImage.objects.create(
        title=request.data['title'], img=request.data['img'])
    serializer = UploadedImageSerializer(img)
    return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_img(request, **kwargs):
    img = UploadedImage.objects.get(id=kwargs.get("img_id"))
    img.delete()
    return Response({'data': 'Image deleted successfully!'}, status=status.HTTP_200_OK)
