#

def test(a, b='str1', *, c='str2'):  # после * только явное указание
    return a, b, c


print(test(10))  # (10, 'str1', 'str2')
print(test(10, '10', c='20'))  # (10, '10', '20')


def get_html(url, headers, *, proxy=None):
    if isinstance(proxy, str):
        print(f'proxy: {proxy}, {url}:{headers}')
    elif proxy is None:
        print(f'proxy: none, {url}:{headers}')


url = 'https://google.com'
headers = 'test'
get_html(url, headers, proxy='121212')
