from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from . models import Cake,Category,Shape,Weight

from . serializers import CakeSerializer,CategorySerializer,ShapeSerializer,WeightSerializer

from rest_framework.authentication import BasicAuthentication,TokenAuthentication

from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from authentication.permissions import IsAdmin,IsUser

from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.

class CakeListCreateView(APIView):

    serializer_class = CakeSerializer

    authentication_classes = [JWTAuthentication]

    # permission_classes = [IsAdminUser]

    def get_permissions(self):

        permissions = []

        if self.request.method == 'POST':

            permissions = [IsAdmin]

        return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        cakes=Cake.objects.all()

        serializer = self.serializer_class(cakes,many=True)

        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid() :

            serializer.save()

            data = {'msg':'cake created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class CakeRetrieveUpdateDestroyView(APIView):

    serializer_class = CakeSerializer

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')

        cake = Cake.objects.get(id=id)

        serializer = self.serializer_class(cake)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')
        
        cake = Cake.objects.get(id=id)

        serializer = self.serializer_class(instance=cake,data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'cake updated successfully '}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')
                
        cake = Cake.objects.get(id=id)

        cake.delete()

        data = {'msg':'cake deleted successfully'}

        return Response(data,status=200)

class CategoryListCreateView(ListCreateAPIView):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    lookup_field = "id"

    queryset = Category.objects.all()
    
    serializer_class = CategorySerializer
    
class ShapeListCreateView(ListCreateAPIView):

    queryset = Shape.objects.all()

    serializer_class = ShapeSerializer

class ShapeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    lookup_field = "id"

    queryset = Shape.objects.all()
    
    serializer_class = ShapeSerializer

class WeightListCreateView(ListCreateAPIView):

    queryset = Weight.objects.all()

    serializer_class = WeightSerializer

class WeightRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    lookup_field = "id"

    queryset = Weight.objects.all()
    
    serializer_class = WeightSerializer
    


        







        
