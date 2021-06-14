from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser 
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
'''
 importing for api_view
'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

'''
for class based view
'''
from rest_framework.views import APIView

'''
for generic based view
'''
from rest_framework import generics
from rest_framework import mixins

'''
	for Authentication
'''
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


'''
	Example of Class Based View
'''

class GenericAPIListall(generics.GenericAPIView,mixins.ListModelMixin):

	serializer_class = ArticleSerializer
	queryset = Article.objects.all()


	def get(self,request):
		return self.list(request)


class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
	mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

	serializer_class = ArticleSerializer
	queryset = Article.objects.all()

	lookup_field = 'id' # required for update the data put method

	'''
	Adding authentication
	'''
	#authentication_classes = [SessionAuthentication,BasicAuthentication]
	#permission_class = [IsAuthenticated]

	authentication_classes = [TokenAuthentication]
	permission_class = [IsAuthenticated]


	def get(self,request,id):
		if id:
			return self.retrieve(request)
		else:
			return self.list(request)

	# For Posting Data

	def post(self,request,id=None):
		return self.create(request,id)

	# For updating data
	def put(self,request,id=None):
		return self.update(request,id)


	# For Delete Method
	def delete(self,request,id):
		return self.destroy(request,id)



'''
	Example of Class Based View
'''
class ArticleAPIView(APIView):
	def get(self,request):
		articles 	= Article.objects.all()# get all the data from the database
		serializer  = ArticleSerializer(articles,many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = ArticleSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
	def get_objects(self,id):
		try:
			return Article.objects.get(id=id)
		except Article.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	def get(self,request,id):
		article = self.get_objects(id)
		serializer = ArticleSerializer(article)
		return Response(serializer.data)

	def put(self,request,id):
		article = self.get_objects(id)
		serializer = ArticleSerializer(article,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id):
		article = self.get_objects(id)
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


'''
	Example of function based views
'''
#@csrf_exempt
@api_view(['GET','POST']) #for api_view
def article_list(request):
	if request.method == 'GET':
		articles 		= Article.objects.all()
		serializer		= ArticleSerializer(articles,many=True) # Queue Reset

		print(serializer.data)
		return Response(serializer.data)
		#return JsonResponse(serializer.data , safe=False)

	elif request.method == 'POST':
		#data 		= JSONParser().parse(request)
		#serializer  = ArticleSerializer(data=data)

		serializer  = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
			#return JsonResponse(serializer.data ,status=201)

		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		#return JsonResponse(serializer.errors,status=400)


#@csrf_exempt
@api_view(['GET','POST']) # for api_view
def article_detail(request,pk):
	try:
		article = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)
		#return HttpResponse(status=404)
		
	if request.method == 'GET':
		serializer 	= ArticleSerializer(article)
		return Response(serializer.data)
		#return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		#data = JSONParser().parse(request)
		#serializer = ArticleSerializer(article,data=data)
		serializer = ArticleSerializer(article,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
			#return JsonResponse(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		#return JsonResponse(serializer.error,status=400)

	elif request.method == 'DELETE':
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		#return HttpResponse(status=204)


