import socket
from tkinter import *
from encryption import encrypt

class ClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("Secure Client")

        self.label = Label(master, text="Enter message:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.send_button = Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

        self.text = Text(master)
        self.text.pack()

        self.password = "Ay0bami@7"

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 65432))

    def log_message(self, message):
        self.text.insert(END, message + "\n")
        self.text.see(END)

    def send_message(self):
        message = self.entry.get()
        if message.lower() == 'exit':
            self.client_socket.close()
            self.master.quit()
        else:
            salt, iv, ciphertext = encrypt(message, self.password)
            self.client_socket.send(salt + iv + ciphertext)
            self.log_message(f"Sent encrypted message: {ciphertext}")

if __name__ == "__main__":
    root = Tk()
    client_gui = ClientGUI(root)
    root.mainloop()
