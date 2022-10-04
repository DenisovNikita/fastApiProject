import grpc
import re

from grpc_example.definitions.builds.service_pb2 import Null, Honey
from grpc_example.definitions.builds.service_pb2_grpc import TestServiceStub

def test_server():
    with grpc.insecure_channel("localhost:3000") as channel:
        client = TestServiceStub(channel)
        client.Health(Null())

        confirmation = client.AddHoney(Honey(
            name="Flower",
            description="Honey from Altay fields with flower flavor",
            price=5000
        ))

        assert re.match("%Y-%m-%d %H:%M:%S", confirmation.date)
