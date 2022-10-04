import grpc

from definitions.builds.service_pb2 import Null, Honey
from definitions.builds.service_pb2_grpc import TestServiceStub


def main():
    with grpc.insecure_channel("localhost:3000") as channel:
        client = TestServiceStub(channel)
        client.Health(Null())

        confirmation = client.AddHoney(Honey(
            name="Flower",
            description="Honey from Altay fields with flower flavor",
            price=5000
        ))

        print(confirmation.date)


if __name__ == "__main__":
    main()
