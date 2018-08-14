#views.py

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
from django.http import JsonResponse
from .models import Entry

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
 
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def entries_list(request, pk):
    entries = Entry.objects.filter(author=pk).values('reason1', 'reason2', 'reason3', 'goal', 'date', 'id') # only grab some attributes from our database, else we can't serialize it.
    entries_list = list(entries)
    return JsonResponse(entries_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.

def entry_detail(request, pk, date):
    entry = Entry.objects.filter(author=pk, date=date).values('reason1', 'reason2', 'reason3', 'goal', 'date', 'id')
    entry_date_list = list(entry)
    return JsonResponse(entry_date_list, safe=False)

