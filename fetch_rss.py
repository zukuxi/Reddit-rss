import urllib.request

# Reddit worldnews 每日最热帖子的 RSS 链接
url = "https://www.reddit.com/r/worldnews/top/.rss?t=day"

# 伪装请求头，防止被 Reddit 拦截
req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 GitHubActions/1.0'
    }
)

try:
    with urllib.request.urlopen(req) as response:
        feed_data = response.read()
        # 将获取到的 RSS 保存为 XML 文件
        with open("worldnews.xml", "wb") as f:
            f.write(feed_data)
    print("RSS 抓取成功！")
except Exception as e:
    print(f"抓取失败: {e}")
