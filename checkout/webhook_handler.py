

from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handle a  payment_intent_succeeded event from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

      def handle_payment_intent_payment_failed(self, event):
        """
        Handle a  payment_intent_payment_failed event from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)