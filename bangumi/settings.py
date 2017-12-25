# -*- coding: utf-8 -*-

# Scrapy settings for bangumi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bangumi'

SPIDER_MODULES = ['bangumi.spiders']
NEWSPIDER_MODULE = 'bangumi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'bangumi (+http://www.yourdomain.com)'

# Obey robots.txt rules

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'bangumi.middlewares.BangumiSpiderMiddleware': 543,
# }
# DOWNLOAD_DELAY = 0.25
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'bangumi.RandomProxy': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 300,
    'bangumi.middlewares.RandomUserAgentMiddleware': 400,
}

# Proxies setting
# Retry many times since proxies often fail
RETRY_TIMES = 3
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = 'list.txt'
# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
# CUSTOM_PROXY = "http://host1:port"



# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': 100,
}

ITEM_PIPELINES = {
    # 'bangumi.pipelines.BangumiAnimateCharacterPipelines': 200,
    'bangumi.pipelines.ImageDownloadPipeline': 400,  # 下载图片
    'bangumi.pipelines.BangumiCharacterPipelines': 100,  # 保存角色信息
    'bangumi.pipelines.BangumiIDPipelines': 2,  # 保存ID
    'bangumi.pipelines.BangumiGamePipelines': 3,  # 保存ID
    'bangumi.pipelines.BangumiAnimatePipelines': 298,  # 保存Animate信息
    'bangumi.pipelines.BangumiBookPipelines': 299,  # 保存Book信息
    'bangumi.pipelines.BangumiPersonPipelines': 300,  # 保存声优信息
    'bangumi.pipelines.BangumiMusicPipelines': 301,  # 保存专辑信息

}
IMAGES_STORE = "H:\\download_img"
IMAGES_EXPIRES = 90  # 过期天数
IMAGES_MIN_HEIGHT = 0  # 图片的最小高度
IMAGES_MIN_WIDTH = 0  # 图片的最小宽度
# Configure model pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
COOKIES_ENABLES = True
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False
DNSCACHE_ENABLED = True
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'ERROR'
LOG_SHORT_NAMES = True
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
