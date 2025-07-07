import requests

def fetch_and_filter_proxies():
    url = "https://80ip.152886.xyz/mzg123456789456/ip80/main/proxyip.txt"
    
    try:
        # 发送GET请求获取网页内容
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        
        # 按行分割内容
        lines = response.text.split('\n')
        
        # 初始化三个列表来存储不同类别的IP
        jp_ips = []
        sg_ips = []
        kr_ips = []
        
        # 遍历每一行
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 检查是否包含433
            if ':433' in line:
                # 检查是否包含JP
                if 'JP' in line:
                    jp_ips.append(line)
                # 检查是否包含SG
                elif 'SG' in line:
                    sg_ips.append(line)
                # 检查是否包含KR
                elif 'KR' in line:
                    kr_ips.append(line)
        
        # 将结果写入不同的文件
        with open('jip.txt', 'w') as f:
            f.write('\n'.join(jp_ips))
        
        with open('sip.txt', 'w') as f:
            f.write('\n'.join(sg_ips))
        
        with open('kip.txt', 'w') as f:
            f.write('\n'.join(kr_ips))
        
        print("代理IP已成功提取并保存到相应文件！")
        
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    fetch_and_filter_proxies()
