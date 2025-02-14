#pip install psycopg2-binary
import psycopg2
import socket


def conn():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    server_address = ('localhost', 8080)

    try:
        # Connect to the server
        client_socket.connect(server_address)
        print("Connected to localhost on port 8080")

        # Send a message to the server
        message = "Hello, Server!"
        client_socket.sendall(message.encode('utf-8'))

        # Receive a response from the server
        response = client_socket.recv(1024)
        print("Received from server:", response.decode('utf-8'))

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        client_socket.close()


def main():
    conn()

main()
