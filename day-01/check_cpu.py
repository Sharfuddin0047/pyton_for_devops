import psutil

def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold: "))
    current_cpu = psutil.cpu_percent(interval=1)
    print("Current_cpu %: ", current_cpu)

    if (current_cpu > cpu_threshold):
        print("CPU Alert, Email Sent...")
    else:
        print("Everything is fine")

check_cpu_threshold()