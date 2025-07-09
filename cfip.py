import requests
from bs4 import BeautifulSoup
import re

def extract_ips_from_webpage(url):
    try:
        # 发送HTTP请求获取网页内容
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找所有的IP地址（这里假设IP是类似192.168.1.1:80的格式）
        # 使用正则表达式匹配IP:PORT格式
        ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d+\b')
        ips = ip_pattern.findall(soup.get_text())
        
        # 只取前100个IP
        return ips[:100]
    except Exception as e:
        print(f"Error fetching or parsing webpage: {e}")
        return []

def save_ips_to_file(ips, output_file='cfip.txt'):  # 修改默认输出文件名为 cfip.txt
    with open(output_file, 'w') as f:
        for i, ip in enumerate(ips, start=1):
            # 写入格式为：IP#优选cf+行号
            f.write(f"{ip}#优选cf{i}\n")

if __name__ == "__main__":
    # 替换为你要提取IP的网页URL
    webpage_url = "https://example.com"  # 请替换为实际的URL
    
    ips = extract_ips_from_webpage(webpage_url)
    if ips:
        save_ips_to_file(ips)
        print(f"成功提取并保存了{len(ips)}个IP到 cfip.txt")  # 更新提示信息
    else:
        print("没有提取到任何IP")
