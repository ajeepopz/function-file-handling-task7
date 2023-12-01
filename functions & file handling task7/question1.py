#timestamp

import os
from datetime import datetime

def timestamp():
    # the current timestamp
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file= f"test_file_{time}.txt"
    
    
    content = f"Content created at {time}"

    try:
       
        with open(file, 'w') as file:
            file.write(content)
        print(f"File '{file}' current date and time")
    except Exception as e:
        print(f"Error: {e}")

timestamp()