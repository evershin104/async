import os
import threading

print(f"Process PID {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"Current num of threads {total_threads}")
print(f"Current name of threads {thread_name}")