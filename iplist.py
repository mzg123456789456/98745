import requests
import re
import os

# 目标URL列表
urls = {
    'jip': 'https://raw.githubusercontent.com/mzg123456789456/98745/refs/heads/main/jip.txt',
    'kip': 'https://raw.githubusercontent.com/mzg123456789456/98745/refs/heads/main/kip.txt',
    'sip': 'https://raw.githubusercontent.com/mzg123456789456/98745/refs/heads/main/sip.txt'
}

# 正则表达式用于匹配IP地址
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# 检查文件是否存在，如果存在则删除
def clear_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

clear_file('ipt.txt')  # 清理最终输出文件

# 国家名称映射
country_map = {
    'jip': '日本',
    'kip': '韩国',
    'sip': '新加坡'
}

# 处理每个URL
with open('ipt.txt', 'w', encoding='utf-8') as output_file:
    for file_type, url in urls.items():
        try:
            # 发送HTTP请求获取内容
            response = requests.get(url)
            response.raise_for_status()
            content = response.text
            
            # 查找IP地址
            ip_match = re.search(ip_pattern, content)
            if ip_match:
                ip = ip_match.group()
                country = country_map[file_type]
                
                # 写入3个格式化IP，每行一个
                for i in range(1, 10):
                    formatted_ip = f"{ip}:443#{country}{i}"
                    output_file.write(formatted_ip + '\n')
                
                print(f'成功处理 {country} IP: {ip}')
            else:
                print(f'未找到IP地址在 {url}')
        except Exception as e:
            print(f'处理 {url} 时出错: {str(e)}')

print('所有IP地址已按行保存到ipt.txt')
