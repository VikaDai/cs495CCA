#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    if request.method == 'POST':
        # Start the stress_cpu.py script in a separate process
        subprocess.Popen(['python', 'stress_cpu.py'])
        return jsonify(message="CPU stress test started"), 200

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return f"Private IP address: {private_ip}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)


# In[ ]:




