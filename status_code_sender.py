import socket, random, time

host = 'localhost'
port = 9999

status_codes = [200, 201, 400, 404, 500, 503]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()

    print(f"Server started on {host}:{port}. Waiting for connections...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
           status_code = str(random.choice(status_codes)) 
           print(f"Sending status code: {status_code}")
           conn.sendall(status_code.encode())
           time.sleep(10)
