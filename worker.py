import os
import zmq
import time

PORT = 5690
HOST = os.environ['SLURM_SUBMIT_HOST'] if 'SLURM_SUBMIT_HOST' in os.environ else 'fidis'
NODE_NAME = os.environ['SLURMD_NODENAME'] if 'SLURMD_NODENAME' in os.environ else 'unknown_node'

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PULL)
sock.connect("tcp://{host}:{port}".format(host=HOST, port=PORT))

i = 0
while i < 10:
    message = sock.recv()
    print("[{node}] Received: {msg}".format(node=NODE_NAME, msg=message))
    i += 1
