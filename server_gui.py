import socket
from tkinter import *
from encryption import decrypt
import threading

class ServerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Secure Server")
        
        self.label = Label(master, text="Server Logs")
        self.label.pack()

        self.text = Text(master)
        self.text.pack()

        self.start_button = Button(master, text="Start Server", command=self.start_server)
        self.start_button.pack()

        self.password = "Ay0bami@7"
        
    def log_message(self, message):
        self.text.insert(END, message + "\n")
        self.text.see(END)

    def handle_client(self, conn):
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                salt, iv, ciphertext = data[:16], data[16:32], data[32:]
                message = decrypt(salt, iv, ciphertext, self.password)
                self.log_message(f"Received encrypted message: {ciphertext}")
                self.log_message(f"Decrypted message: {message}")
        except Exception as e:
            self.log_message(f"An error occurred: {e}")
        finally:
            conn.close()

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 65432))
        server_socket.listen(1)
        self.log_message("Server listening on port 65432...")

        def accept_connections():
            while True:
                conn, addr = server_socket.accept()
                self.log_message(f"Connection from {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(conn,))
                client_thread.start()

        accept_thread = threading.Thread(target=accept_connections)
        accept_thread.start()

if __name__ == "__main__":
    root = Tk()
    server_gui = ServerGUI(root)
    root.mainloop()
