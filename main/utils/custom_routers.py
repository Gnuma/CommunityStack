from rest_framework.routers import SimpleRouter, Route

class RetrieveByCategoryRouter(SimpleRouter):

    routes = [
       Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=True,
            initkwargs={'suffix': 'List'}
        ),
    ]