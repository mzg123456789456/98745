import requests
from datetime import datetime

def fetch_and_filter_proxies():
    url = "https://80ip.152886.xyz/mzg123456789456/ip80/main/proxyip.txt"
    log_message = ""
    
    try:
        # 添加请求头模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        lines = response.text.split('\n')
        jp_ips = []
        sg_ips = []
        kr_ips = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if ':433' in line:
                if 'JP' in line.upper():
                    jp_ips.append(line)
                elif 'SG' in line.upper():
                    sg_ips.append(line)
                elif 'KR' in line.upper():
                    kr_ips.append(line)
        
        # 写入文件并添加时间戳
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"# 最后更新: {timestamp}\n# 总数: {len(jp_ips)}\n\n"
        
        with open('jip.txt', 'w') as f:
            f.write(header + '\n'.join(jp_ips))
            
        with open('sip.txt', 'w') as f:
            f.write(header + '\n'.join(sg_ips))
            
        with open('kip.txt', 'w') as f:
            f.write(header + '\n'.join(kr_ips))
        
        log_message = f"成功更新代理列表 | JP: {len(jp_ips)} | SG: {len(sg_ips)} | KR: {len(kr_ips)}"
        print(log_message)
        
    except Exception as e:
        log_message = f"更新失败: {str(e)}"
        print(log_message)
    finally:
        # 写入日志
        with open('proxy_update.log', 'a') as log_file:
            log_file.write(f"{datetime.now().isoformat()} - {log_message}\n")

if __name__ == "__main__":
    fetch_and_filter_proxies()
