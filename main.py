#from func.getsite import get_site
#from func.getproxy import get_proxy
import concurrent.futures
from xbrowser import run_browser

# List of ports to use for proxies
ports = [7100, 7101, 7102]

# Number of threads to use
num_threads = len(ports)

def main():
    # Create ThreadPoolExecutor with num_threads threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Create a future for each thread and add it to the executor
        futures = [executor.submit(lambda port: run_browser('https://browserleaks.com/javascript'), port) for port in ports]
        
        # Wait for all futures to complete
        for future in concurrent.futures.as_completed(futures):
            # If any of the futures raise an exception, print the exception
            # and re-raise it so the program will exit with a non-zero exit code
            if future.exception() is not None:
                print(future.exception())
                raise future.exception()

if __name__ == '__main__':
    main()
