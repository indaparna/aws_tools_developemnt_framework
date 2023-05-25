import yaml
from yaml.loader import SafeLoader
import json
from pytz import timezone 
from datetime import datetime
import pytz


def jsonify_string(input_string):
    """
    Converts the Input String to Json Dictionary
    """
    return json.loads(input_string)


def load_yaml_file(input_yaml_file_path):
    """
    Read YAML document(s) from a givn file path
    """
    with open(input_yaml_file_path, 'r') as f:
        data = list(yaml.load_all(f, Loader=SafeLoader))

    return data


def load_document_in_yaml_file(document_name, yaml_file_path):
    """
    Return a required document from the entire YAML file(list of documents) 
    """
    required_api_index = -1

    yaml_data = load_yaml_file(yaml_file_path)
    for document in yaml_data:
        if document['name'] == document_name:
            required_api_index = yaml_data.index(document)
            break

    return yaml_data[required_api_index]


def pretty_print_json(input_dict):
    """
    This function takes a JSON dictionary as input and prints it in a
    pretty format. The output is indented by 4 spaces.

    Args:
        input_dict: The JSON dictionary to be printed.

    Returns:
        The formatted JSON string.
    """

    formatted_data = json.dumps(input_dict, indent=4)
    print(formatted_data)
    return formatted_data


def get_current_timestamp(timestamp_format="%d_%m_%Y__%H_%M_%S_%f"):
    """
    Get IST Time based Timestamp
    """
    # timestamp_format = '%d_%m_%Y__%H_%M_%S_%f'
    return datetime.now(timezone("Asia/Kolkata")).strftime(timestamp_format)


def append_to_file(file_data, file_name):
    """
    This function appends the given data to the specified file.

    Args:
        file_data: The data to be appended to the file.
        file_name: The name of the file to be appended to.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an I/O error occurs while appending to the file.
    """
    f = open(file_name, "a")
    f.write(file_data)
    f.close()


def write_to_file(file_data, file_name):
    """
    This function writes the given data to the specified file.

    Args:
        file_data: The data to be written to the file.
        file_name: The name of the file to be written to.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an I/O error occurs while writing to the file.
    """
    f = open(file_name, "w")
    f.write(file_data)
    f.close()


def read_file(file_name):
    """
    This function reads the contents of the specified file.

    Args:
        file_name: The name of the file to be read.

    Returns:
        The contents of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an I/O error occurs while reading the file.
    """
    f = open(file_name, "r")
    file_data = f.read()

    return file_data

def convert_utc_to_ist(input_timestamp):
    """
    This function converts a UTC timestamp to an Indian Standard Time (IST) timestamp.

    Args:
        input_timestamp: The UTC timestamp to be converted.

    Returns:
        The IST timestamp as a string.
    """
    
    INPUT_UTC_TIMESTAMP_FORMAT="%Y-%m-%dT%H:%M:%S.%fZ"
    
    OUTPUT_TIMEZONE="Asia/Kolkata"
    OUTPUT_TIMESTAMP_FORMAT="%Y-%m-%d %H:%M:%S"
    
    input_time = datetime.strptime(input_timestamp, INPUT_UTC_TIMESTAMP_FORMAT)
    input_time = pytz.utc.localize(input_time)
    
    output_timezone = pytz.timezone(OUTPUT_TIMEZONE)
    output_time = input_time.astimezone(output_timezone)
    return output_time.strftime(OUTPUT_TIMESTAMP_FORMAT)

# if __name__ == '__main__':
#     print(get_current_timestamp())