from rest_framework import serializers
from datetime import date, timedelta

from account.models import User
from subscription.models import Plan, Subscription


# PLAN
class PlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

# SUBSCRIPTION
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            'id',
            'name',
            'slug',
            'price'
        )

class SubscriptionListSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    
    class Meta:
        model = Subscription
        fields = '__all__'
        # exclude = ('user',)

# SUBSCRIBE
# Stripe subscription sistemi öğren
# Without stripe
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        exclude = ['user']
        extra_kwargs = {
            'paid_amount': {
                'read_only': True
            }
        }
    
    def create(self, validated_data):
        plan = validated_data.get('plan')
        user = self.context.get('request').user
        period_type = validated_data.get('period_type')

        # customer = stripe.Customer.create(
        #     email=self.context['request'].user.email,
        #     source=token
        # )

        if period_type == 0:
            period_duration = 30
            paid_amount = plan.price
        else:
            period_duration = 365
            paid_amount = (plan.price * 10)

        start_date = date.today()
        expiry_date = start_date + timedelta(days=period_duration)

        subscription_object = Subscription.objects.create(
            user=user,
            plan=plan,
            period_type=period_type,
            period_duration=period_duration,
            start_date=start_date,
            expiry_date=expiry_date,
            paid_amount=paid_amount,
            is_active=True
        )

        return subscription_object

