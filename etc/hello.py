CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web',
    'python': '/usr/bin/python',
    'args': (
        '--bind=127.0.0.1:8080',
        '--workers=16',
        '--timeout=60',
		'--log-level=debug',
        'hello.py',
    ),
}
