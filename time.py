import zmq
from datetime import datetime

def time_server():
    context = zmq.Context
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Time server is running on port 5555...")

    while True:
        message = socket.recv_string()
        if message == "GET_DATE":
            current_date = datetime.now().strftime("%Y-%m-%d")
            socket.send_string(current_date)
        elif message == "GET_DATE_TIME":
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            socket.send_string(current_time)
        elif message == "GET_TIME":
            current_time = datetime.now().strftime("%H:%M:%S")
            socket.send_string(current_time)
        else:
            socket.send_string("Error: Invalid Request")


if __name__ == "__main__":
    time_server()