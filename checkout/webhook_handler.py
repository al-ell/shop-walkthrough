from django.http import HttpResponse

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):

        return HttpResponse(
            ceontent=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):

        return HttpResponse(
            ceontent=f'Webhook recieved: {event["type"]}',
            status=200)
    
    def handle_paymen_intent_failed(self, event):

        return HttpResponse(
            ceontent=f'Webhook recieved: {event["type"]}',
            status=200)
