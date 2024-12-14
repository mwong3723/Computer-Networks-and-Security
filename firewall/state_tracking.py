# state_tracking.py

STATE_TABLE = {}

def track_connection(ip_src, ip_dst, sport, dport):
    connection_key = (ip_src, ip_dst, sport, dport)
    if connection_key not in STATE_TABLE:
        STATE_TABLE[connection_key] = 'ESTABLISHED'
        print(f"New connection: {connection_key}")
    else:
        print(f"Connection {connection_key} already exists.")
