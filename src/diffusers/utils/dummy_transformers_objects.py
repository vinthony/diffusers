# This file is autogenerated by the command `make fix-copies`, do not edit.
# flake8: noqa
from ..utils import DummyObject, requires_backends


class GLIDESuperResUNetModel(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])


class GLIDETextToImageUNetModel(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])


class GLIDEUNetModel(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])


class UNetGradTTSModel(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])


GLIDE = None


class GradTTS(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])


class LatentDiffusion(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])