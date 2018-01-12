#!/usr/bin/env python

import sys
import s3fs 
from termcolor import colored
import pandas as pd

from s3fs_patch import s3
from config import default_params_sets


def preview_file(params):
    """
    s3 bucket files paths are expected to have this format:

      s3://{bucket}/logs/{version-date}/transform/{run-time}/{after-time}/{filename}

    Parameters
    ----------
    params: dict
        should have the keys 'pre' and 'after-time'
    """
    raw_times = [f.split("/")[-1] for f in s3.ls(params['pre'])]
    datetimes = pd.to_datetime(pd.Series(raw_times), format="%Y-%m-%d_%H.%M.%S")
    most_recent_str = datetimes.max().strftime("%Y-%m-%d_%H.%M.%S")

    next_pre = params['pre'] + most_recent_str + params['after-time']

    files = s3.ls(next_pre)
    filepath = files[int(file_number)]
    with s3.open(filepath, 'rb') as f:
        contents = f.read()
        print(colored(contents, 'yellow'))
    
    print(colored("---------------", "cyan"))
    print(colored("---------------", "cyan"))
    print(colored("---------------", "cyan"))
    print(colored("This traceback came from the file: ", "cyan"))
    print("")
    print(colored(filepath, "cyan"))


if __name__ == '__main__':

    if len(sys.argv) == 1:
        raise AssertionError("must provide parameter key." \
                " Available sets are: {}".format(default_params_sets.keys()))

    param_key = sys.argv[1]

    if len(sys.argv) == 2:
        file_number = 0
    else:
        file_number = sys.argv[2]

    params = default_params_sets.get(param_key)
    if not params:
        raise AssertionError("{} does not match any available param sets" \
                " available sets are: {}".format(param_key, 
                                                 default_params_sets.keys()))

    preview_file(params)
