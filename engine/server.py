import grpc
from concurrent import futures
import time

import calculator_pb2
import calculator_pb2_grpc
import calculator

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    #calculator.square_root is exposed here
    # the request and response are of the data type calculator_pb2.Number
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#use the generated function `add_CalculatorServicer_to_server` to add the defined class to the server
calculator_pb2_grpc.add_CalculatorServicer_to_server(
    CalculatorServicer(), server
)

#listen on port 50051
print('Starting server. Listening on port 50051')
server.add_insecure_port('[::]:50051') #[::] represents the wildcard IPv6 address, meaning the server will listen on all available network interfaces. The port number 50051 is the specific port on which the server will listen.
server.start()


#since server.start() will not block, a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
