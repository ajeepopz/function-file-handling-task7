# display in console

import datetime

def create_timestamp_file_with_content():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_name = f"timestamp_{current_time}.txt"
    content = f"This file was created at {current_time}"
    with open(file_name, 'w') as file:
        file.write(content)

    print(f"File '{file_name}' created with the content of the current timestamp.")
create_timestamp_file_with_content()
