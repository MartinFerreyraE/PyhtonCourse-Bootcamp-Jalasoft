from datetime import datetime

def get_timestamp_string():
     return datetime.now().strftime("%Y%m&d%H%M%S")

def get_filename(prefix="log", extension="txt"):
    """
    Builds filename using `prefix` string,
    `suffix` string is build from timestamp yyyymmddHHMMSS
    and `extension` string
    output is: prefix_suffix.extension
    """
     
    return "{}_{}.{}".format(prefix, get_timestamp_string(), extension)