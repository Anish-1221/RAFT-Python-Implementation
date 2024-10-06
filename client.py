import grpc
import raft_pb2
import raft_pb2_grpc

def run():
    try:
        while True:
            # Connect to the gRPC server (make sure the port matches the server port)
            with grpc.insecure_channel('localhost:9001') as channel:  # Adjust to your server's port
                stub = raft_pb2_grpc.RaftNodeStub(channel)

                # Send a HeartbeatMessage to the server
                heartbeat_request = raft_pb2.heartbeatMessage(leader_name="Leader1", leader_port=12345)
                response = stub.ackHeartbeat(heartbeat_request)
                print(f"Server response: {response.message}")

                # Send a LogMessage to append to the log
                log_request = raft_pb2.logMessage(index=0, key="1", value="3", instruction="INSERT")
                log_response = stub.logAppend(log_request)
                print(f"Server response: {log_response.message}")

                # Implement logCommit
                
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    run()