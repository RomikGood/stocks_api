from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StockAPIViewset(APIViewSet):
    def retrieve(self, request, id=None):
        # http :6543/api/v1/stock/{id}/

        # Use the `id` to lookup that resource in the DB,
        # Formulate a response and send it back to the client
        return Response(
            json={'message': 'Provided a single resource'},
            status=200
        )

    def list(self, request):
        return Response(
            json={'message': 'Provided a list of stocks'},
            status=200
        )

    def create(self, request):
        import pdb; pdb.set_trace()
        return Response(
            json={'message': 'Created a new resource'},
            status=201
        )

    def destroy(self, request, id=None):
        return Response(status=204)