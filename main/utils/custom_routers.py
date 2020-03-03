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

"""
Questi due sono uguali, non dovevi farne un altro.
"""
class RetrieveByTopicRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={
                'get': 'list',
            },
            name='{basename}-list',
            detail=True,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'post': 'create',
            },
            name='{basename}-create',
            detail=False,
            initkwargs={'suffix': 'Create'}
        )
    ]
