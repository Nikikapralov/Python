from urllib import parse


def decode(url):
    new_url = parse.unquote(url)
    return new_url


def get_parts(result):
    protocol = get_protocol(result)
    host, port = get_host_port(result, protocol)
    path = get_path(result)
    query = result.query
    if not is_valid(host, port, protocol, path):
        return 'Invalid URL'
    fragment = result.fragment
    return {'Protocol': protocol, 'Host': host, 'Port': port, 'Path': path, 'Query': query, 'Fragment': fragment}


def is_valid(host, port, protocol, path):
    return all([protocol, host, port, path])


def print_result(dictionary):
    [print(f'{key}: {value}') for key, value in dictionary.items() if value]


def get_protocol(result):
    if result.scheme in ('http', 'https'):
        return result.scheme
    return None


def get_host_port(result, protocol):
    if ':' in result.netloc:
        host, port = result.netloc.split(':')
        return host, port
    elif '.' in result.netloc:
        host = result.netloc
        if protocol == 'http':
            port = 80
        elif protocol == 'https':
            port = 443
        return host, port
    return None, None


def get_path(result):
    path = result.path
    if not path:
        path = '/'
    return path

def main(url):
    new_url = decode(url)
    result = parse.urlparse(new_url)
    dictionary = get_parts(result)
    if dictionary == 'Invalid URL':
        print(dictionary)
        return
    print_result(dictionary)

main('https://mysite:80/demo/index.aspx')
main('somesite.com:80/search?')
main('https/mysite.bg?id=2')
main('https://my-site.bg')
main('https://mysite.bg/demo/search?id=22o#go')
main('https://softuni.bg:447/search?Query=pesho&Users=true#go')
main('http://softuni.bg/')