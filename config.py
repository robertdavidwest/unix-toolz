

default_params_sets = {

    'lds-transform-reruns': { 
        'job': 'preview',
        'pre': 's3://rmdy-analytics-lds-out/logs/11.20.2017/transform/',
        'after-time': '/reruns_needed/'
    },
    'lds-transform-completed': { 
        'job': 'count',
        'pre': 's3://rmdy-analytics-lds-out/logs/11.20.2017/transform/',
        'after-time': '/completed/'
    }
}
    
