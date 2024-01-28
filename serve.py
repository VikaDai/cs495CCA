{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, jsonify\
import subprocess\
import socket\
\
app = Flask(__name__)\
\
@app.route('/', methods=['POST'])\
def stress_cpu():\
    if request.method == 'POST':\
        # Start the stress_cpu.py script in a separate process\
        subprocess.Popen(['python', 'stress_cpu.py'])\
        return jsonify(message="CPU stress test started"), 200\
\
@app.route('/', methods=['GET'])\
def get_private_ip():\
    # Get the private IP address\
    hostname = socket.gethostname()\
    private_ip = socket.gethostbyname(hostname)\
    return jsonify(private_ip=private_ip), 200\
\
if __name__ == '__main__':\
    app.run(host='0.0.0.0', port=5001)\
}