

default_params_sets = {

    'lds-transform-reruns': { 
        'job': 'preview',
        'pre': 's3://rmdy-analytics-lds-out/logs/11.20.2017/transform/',
        'run-time': 'use-latest', #'2018-01-10_15.26.14',  # 'use-latest'
        'after-time': '/reruns_needed/'
    },
    'lds-transform-completed': { 
        'job': 'count',
        'pre': 's3://rmdy-analytics-lds-out/logs/11.20.2017/transform/',
        'run-time':  'use-latest', #'2018-01-10_15.26.14', # 'use-latest'
        'after-time': '/completed/'
    },
}
    
