from rest_framework.views import APIView
from rest_framework.response import Response

class TotalViewsView(APIView):
    """
    Returns total number of video views across all platforms
    """
    def get(self, request):
        return Response({'total_views': 123456789} )
