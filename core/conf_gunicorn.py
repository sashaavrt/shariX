#bind = "0.0.0.0:8001"
import core.config as conf
bind = conf.BIND
workers = conf.WORKERS
worker_class = "sync"
threads = conf.THREADS
timeout = 30
max_requests = 1000
capture_output = True
