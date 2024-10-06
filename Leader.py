from Node import Node
from random import randint
import time
import grpc
from concurrent.futures import ThreadPoolExecutor
import raft_pb2
import raft_pb2_grpc
import globals

# Inheritance
class Leader(Node):
    def __init__(self):
        Node.__init__(self)
        self.type = "leader"

    def sendHeartbeat(self):
        def sendHeartbeat_to_follower(node_name, node_info):
            if node_name != self.name and node_info[1] == "active":
                print(node_name)
                with grpc.insecure_channel(f'localhost:{node_info[0]}') as channel:  # Adjust to your server's port
                    stub = raft_pb2_grpc.RaftNodeStub(channel)

                    # Send a HeartbeatMessage to the server
                    heartbeat_request = raft_pb2.heartbeatMessage(leader_name=self.name, leader_port=globals.servers[self.name][0])
                    response = stub.ackHeartbeat(heartbeat_request)
                    print(f"Follower response: {response.message}")

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(sendHeartbeat_to_follower, key, value) for key, value in globals.servers.items()]

    def sendLogMessage(self):
        leader_log_response = self.logAppend(raft_pb2.logMessage(index=0, key="1", value="3", instruction="INSERT"), context=True)
        print(f"Leader response: {leader_log_response.message}")

        def sendLogMessage_to_follower(node_name, node_info):
            if node_name != self.name and node_info[1] == "active":
                with grpc.insecure_channel(f'localhost:{node_info[0]}') as channel:  # Adjust to your server's port
                    stub = raft_pb2_grpc.RaftNodeStub(channel)

                    # Send a LogMessage to append to the log
                    log_request = raft_pb2.logMessage(index=0, key="1", value="3", instruction="INSERT")
                    log_response = stub.logAppend(log_request)
                    print(f"Follower response: {log_response.message}")

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(sendLogMessage_to_follower, key, value) for key, value in globals.servers.items()]

        # The run method to periodically send heartbeats and log messages
    def run(self):
        try:
            while True:
                print(f"Leader {self.name} sending heartbeats...")
                self.sendHeartbeat()

                print(f"Leader {self.name} sending log messages...")
                self.sendLogMessage()

                # Sleep for a while before sending the next set of heartbeats and logs
                time.sleep(5)  # For example, send every 5 seconds
        except KeyboardInterrupt:
            print("Stopping the leader node...")
            self.server.stop(0)

if __name__ == "__main__":
    leader = Leader()
    leader.run()