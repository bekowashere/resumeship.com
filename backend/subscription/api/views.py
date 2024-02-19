# REST FRAMEWORK
from rest_framework.response import Response
from rest_framework import status

# REST FRAMEWORK VIEWS
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

# PERMISSIONS
from rest_framework.permissions import IsAuthenticated

# MODELS
from subscription.models import Plan, Subscription
from account.models import User

# SERIALIZERS
from subscription.api.serializers import (
    PlanSerializer,
    PlanListSerializer,
    SubscriptionListSerializer,
    SubscriptionSerializer
)

class PlanListAPIView(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanListSerializer

class PlanDetailAPIView(RetrieveAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanListSerializer
    lookup_field = 'id'

class SubscriptionListAPIView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionListSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = Subscription.objects.filter(user=user)
    #     return queryset

class SubscriptionDetailAPIView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionListSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class SubscribeView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()

            response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Your subscription has been successfully created',
                'data': serializer.data
            }

            return Response(response, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
