from rest_framework import generics, permissions, authentication
from rest_framework import mixins

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None or content.strip() == '':
            content = title
        serializer.save(content=content)



class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]


    def perform_update(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None or content.strip() == "":
            content = title
            print(title, content)
        serializer.save(content=content)



class ProductCRUD(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    
    '''this is a class view for handle all the crud of Product model'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):

        if kwargs.get('pk') is not None:
           return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

    def saving_content_as_title(self, serializer):
        '''custom method for both put an post
        saves the content as the title if user dont provide a content'''
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None or content.strip() == '':
            content = title
        serializer.save(content=content)


    def perform_create(self, serializer):
        self.saving_content_as_title(serializer)

    def perform_update(self, serializer):
        self.saving_content_as_title(serializer)
    