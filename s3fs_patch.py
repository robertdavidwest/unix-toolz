from s3fs import S3FileSystem
from s3fs.core import split_path


def _lsdir(self, path, refresh=False):
    if path.startswith('s3://'):
        path = path[len('s3://'):]
    path = path.rstrip('/')
    bucket, prefix = split_path(path)
    prefix = prefix + '/' if prefix else ""
    if path not in self.dirs or refresh:
        try:
            pag = self.s3.get_paginator('list_objects_v2')
            it = pag.paginate(Bucket=bucket, Prefix=prefix, Delimiter='/',
                              **self.req_kw)
            files = []
            dirs = []
            for i in it:
                dirs.extend(i.get('CommonPrefixes', []))
                files.extend(i.get('Contents', []))
            if dirs:
                files.extend([{'Key': l['Prefix'][:-1], 'Size': 0,
                               'StorageClass': "DIRECTORY"} for l in dirs])
                files = [f for f in files if len(f['Key']) > len(prefix)]
            for f in files:
                f['Key'] = '/'.join([bucket, f['Key']])
        except ClientError:
            # path not accessible
            files = []
        self.dirs[path] = files
    return self.dirs[path]

S3FileSystem._lsdir = _lsdir
s3 = S3FileSystem(anon=False)
