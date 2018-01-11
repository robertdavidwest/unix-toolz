

default_params = {
    'pre': 's3://your-bucket-name/any-file-prefix',
    'use-latest': True,  # if True then an 'ls' operation will be performed using
                         # the pre. The results will be converted to dates
                         # then the latest will be used in the file path
    'filename': 'something.txt'
}
