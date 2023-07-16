def listen_for_data():
    paths_methods = {}
    while True:
        data = input()
        if data == 'END':
            break
        path = data[:data.rindex('/')]
        method = data[data.rindex('/') + 1:]
        if path not in paths_methods:
            paths_methods[path] = [method]
        else:
            paths_methods[path].append(method)
    return paths_methods


def get_request():
    data = input()
    method, path, obsolete = data.split()
    return method.lower(), path


def is_ok_or_not(request_method, request_path, paths_methods):
    if request_path not in paths_methods:
        return '404 Not Found', 'Not found', 9

    if request_method not in paths_methods[request_path]:
        return '404 Not Found', 'Not found', 9

    return '200 OK', 'OK', 2


def print_output(status_code, status_text, length):
    print(f'HTTP/1.1 {status_code}\n'
          f'Content-Length: {length}\n'
          f'Content-Type: text/plain\n'
          f'\n'
          f'{status_text}')


def main():
    paths_methods = listen_for_data()
    request_method, request_path = get_request()
    status_code, status_text, length = is_ok_or_not(request_method, request_path, paths_methods)
    print_output(status_code, status_text, length)


main()



