##Bangumi Spider
该项目由是对网站[Bangumi 番组计划](http://bangumi.tv/) 网站的爬虫

###需求
1. Python3.6  
2. Scrapy
3. MongoDB
###爬取器(Spider)
爬取动画，音乐等信息时会下载其封面
1. bangumi_animate_id 爬取需要的Animate(动画)的ID
2. bangumi_music_id 爬取需要的Music（音乐）的ID
3. bangumi_book_id 爬取需要的Book（书籍）的ID
4. bangumi_person_id 爬取需要的Person（三次元人物）的ID
5. bangumi_character_id 爬取需要的Character（二次元人物）的ID
6. bangumi_game_id 爬取需要的Game（游戏）的ID
7. bangumi_animate 爬取需要的Animate(动画)
2. bangumi_music 爬取需要的Music（音乐）
3. bangumi_book 爬取需要的Book（书籍）
4. bangumi_person 爬取需要的Person（三次元人物）
5. bangumi_character 爬取需要的Character（二次元人物）
6. bangumi_game 爬取需要的Game（游戏）
###注意事项
1. 请在init中配置MongoDB相关的连接数据
2. 请在setting中配置图片下载路径
3. 默认打开代理，可以在setting中关闭，根目录下的list文件中写入代理地址作为代理池
###License（MIT）
```
MIT License

Copyright (c) 2017 AllenTom aka TakayamaAren

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```