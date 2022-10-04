from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import grpc

from definitions.builds.service_pb2 import Confirmation
from definitions.builds.service_pb2_grpc import TestServiceServicer, add_TestServiceServicer_to_server


class Service(TestServiceServicer):
    def Health(self, request, context):
        return request

    def AddHoney(self, request, context):
        expected_dateline = datetime.utcnow()
        return Confirmation(date=expected_dateline.strftime("%Y-%m-%d %H:%M:%S"))


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TestServiceServicer_to_server(Service(), server)
    server.add_insecure_port("localhost:3000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
