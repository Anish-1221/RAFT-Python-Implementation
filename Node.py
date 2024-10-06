from random import randint
import time
import grpc
from concurrent import futures
import raft_pb2
import raft_pb2_grpc
import globals


class Node:
    def __init__(self) -> None:
        self.type = "follower"
        self.timer = randint(0, 10)
        self.state = {}
        self.term = 0
        self.port = 9000 + len(globals.servers) + 1
        self.log = []
        self.status = "active"
        self.name = "raftserver" + str(len(globals.servers) + 1)
        globals.servers[self.name] = [self.port, self.status]

        globals.save_servers()

        #partition membership

        # Start gRPC server
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        raft_pb2_grpc.add_RaftNodeServicer_to_server(self, self.server)
        self.server.add_insecure_port(f'[::]:{self.port}')
        print(f"Server is listening on port {self.port}")
        self.server.start()

    def timeout(self):
        # wait for timer milliseconds
        print(f"Node {self.name} waiting for {self.timer} seconds")
        time.sleep(self.timer)
    
    def ackHeartbeat(self, request, context):
        leader_name = request.leader_name
        leader_port = request.leader_port
        print(f"Received heartbeat from leader {leader_name} on port {leader_port}")

        # Return the last log value [index, {key: value}, instruction]

        return raft_pb2.ackMessage(success=True, message=f"Acknowledged heartbeat from leader {leader_name}")


    def logAppend(self, request, context): # message = [index, {key: value}, instruction]
        log_entry = [request.index, {request.key: request.value}, request.instruction]
        self.log.append(log_entry)
        print(f"Log appended: {log_entry}")

        # Return the last log value [index, {key: value}, instruction]

        return raft_pb2.ackMessage(success=True, message=f"Log appended successfully {log_entry}")
    
    def run(self):
        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            self.server.stop(0)

if __name__ == "__main__":
    node = Node()
    node.run()