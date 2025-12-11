# backend/gunicorn.conf.py
"""
This file is loaded by: gunicorn -c gunicorn.conf.py rteknoloji.wsgi:application
"""

import multiprocessing
from pathlib import Path

# Base directory inside the container
BASE_DIR = Path(__file__).resolve().parent

# -----------------------------
# Core server settings
# -----------------------------

# Bind to all interfaces, port 8000 (nginx will talk to this)
bind = "0.0.0.0:8000"

# If you ever want to derive dynamically:
cpu_count = multiprocessing.cpu_count()
workers = max(2, min(cpu_count, 3))

# Simple, predictable worker model.
worker_class = "sync"

# -----------------------------
# Timeouts & connection behavior
# -----------------------------

# Seconds before killing a worker handling a request.
timeout = 60

# Extra time given to workers to gracefully finish requests on reload/shutdown.
graceful_timeout = 30

# Keep-alive for Nginx ↔ Gunicorn connections.
keepalive = 5

# -----------------------------
# Process lifecycle hardening
# -----------------------------

# Recycle workers periodically to avoid memory leaks.
max_requests = 1000
max_requests_jitter = 200

# Load Django once in the master, then fork workers.
# If this ever causes weird DB behavior, set to False.
preload_app = True

# Optional: put temp files on tmpfs for slightly faster I/O.
worker_tmp_dir = "/dev/shm"

# -----------------------------
# Logging
# -----------------------------

# Send all logs to stdout/stderr; Docker will collect them.
accesslog = "-"  # access logs to stdout
errorlog = "-"   # error logs to stderr

# Reasonable default for production; adjust if too noisy.
loglevel = "info"

# Capture print() and other bare writes from the app.
capture_output = True

# -----------------------------
# Request / header limits
# -----------------------------

# Allow reasonably long URLs (e.g., DRF filters) but cap them.
limit_request_line = 8192  # bytes

# Limit number of headers and their size (basic safety).
limit_request_fields = 100
limit_request_field_size = 8190  # bytes

# -----------------------------
# Misc
# -----------------------------

# Ensure we run from /app (just in case).
chdir = str(BASE_DIR)
