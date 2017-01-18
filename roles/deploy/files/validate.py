#!/usr/bin/python
import requests
import sys


def default():
    url = 'http://127.0.0.1:5000/'
    r = requests.get(url, timeout=3.0)
    if r.status_code == 200:
        print('SUCCESS! Response code: ' + str(r.status_code))
        sys.exit(0)
    else:
        print('FAILED. Response code: ' + str(r.status_code))
        sys.exit(2)


if __name__ == "__main__":
    try:
        default()
    except Exception as e:
        print('EXCEPTION_RAISED: ' + str(e))
        sys.exit(3)
    except KeyboardInterrupt:
        sys.exit(1)
