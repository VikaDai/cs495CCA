#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def handle_requests():
    if request.method == "POST":
        # Handle POST request to stress CPU
        stress_cpu_process = subprocess.Popen(["python", "stress_cpu.py"])
        return "Stressing CPU initiated\n"

    elif request.method == "GET":
        # Handle GET request to return private IP address
        private_ip = socket.gethostbyname(socket.gethostname())
        return f"Private IP address: {private_ip}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


# In[ ]:




