

default_params_sets = {

    'lds-{process}-reruns': { 
        'job': 'preview',
        'pre': 's3://{bucket}/logs/11.20.2017/{process}/',
        'after-time': '/reruns_needed/'
    },
    'lds-{process}-completed': { 
        'job': 'count',
        'pre': 's3://{bucket}/logs/11.20.2017/{process}/',
        'after-time': '/completed/'
    }
}
    
