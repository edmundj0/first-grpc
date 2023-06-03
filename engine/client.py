import grpc

#import generated classes
import calculator_pb2
import calculator_pb2_grpc

#open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

#create valid request message
number = calculator_pb2.Number(value=16345345)

stub = calculator_pb2_grpc.CalculatorStub(channel)

#make call
response = stub.SquareRoot(number)

print(response.value)
