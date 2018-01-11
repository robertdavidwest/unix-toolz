import sys
import s3fs 
from termcolor import colored
import pandas as pd

from config import default_params_sets


def preview_file(params):
    s3 = s3fs.S3FileSystem()

    raw_times = [f.split("/")[-1] for f in s3.ls(params['pre'])]
    datetimes = pd.to_datetime(pd.Series(raw_times), format="%Y-%m-%d_%H.%M.%S")
    most_recent_str = datetimes.max().strftime("%Y-%m-%d_%H.%M.%S")

    next_pre = params['pre'] + most_recent_str + params['after-time']

    files = s3.ls(next_pre)
    filepath = files[int(file_number)]
    with s3.open(filepath, 'rb') as f:
        contents = f.read()
        print(colored(contents, 'yellow'))
    
    print("---------------")
    print("---------------")
    print("---------------")
    print("This traceback came from the file: ")
    print("")
    print(filepath)

if __name__ == '__main__':

    if len(sys.argv) == 1:
        raise AssertionError("must provide parameter key")

    param_key = sys.argv[1]

    if len(sys.argv) == 2:
        file_number = 0
    else:
        file_number = sys.argv[2]

    params = default_params_sets.get(param_key)
    if not params:
        raise AssertionError("{} does not match any available param sets" \
                " avilable sets are: ".format(param_key, default_params_sets.keys()))

    preview_file(params)
