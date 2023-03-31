from typing import Protocol, OrderedDict
from . import models


class UserReposInterface(Protocol):
    def create_user(self, data: OrderedDict) -> models.User:
        ...


class UserReposV1:
    model = models.User

    def create_user(self, data: OrderedDict) -> models.User:
        return self.model.objects.create_user(**data)
