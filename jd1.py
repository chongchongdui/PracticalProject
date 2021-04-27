from selenium import webdriver
from time import sleep
import pandas as pd
pd.set_option('display.max_columns', None)    # 显示所有列
pd.set_option('display.max_rows', None)
driver=webdriver.Chrome(executable_path="D:/Users/Anaconda3/chromedriver.exe")
driver.get("https://www.jd.com")
#找到搜索框
driver.find_element_by_xpath("//*[@id='key']").send_keys("编程书籍")
#点击按钮
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button/i").click()

driver.implicitly_wait(5)#休息5s
hrefs=[]
names=[]
prices=[]
commits=[]
shops=[]
for j in range(1,2):
    for i in range(1, 11):
        href = driver.find_element_by_xpath(
            "//ul[@class='gl-warp clearfix']/li[" + str(i) + "]//div[@class='p-img']/a").get_attribute("href")
        price = driver.find_element_by_xpath(
            "//ul[@class='gl-warp clearfix']/li[" + str(i) + "]//div[@class='p-price']")
        name = driver.find_element_by_xpath(
            "//ul[@class='gl-warp clearfix']/li[" + str(i) + "]//div[@class='p-name']//em")   #//*[@id="J_goodsList"]/ul/li[4]/div/div[3]/a/em
        commit = driver.find_element_by_xpath(
            "//ul[@class='gl-warp clearfix']/li[" + str(i) + "]//div[@class='p-commit']/strong")
        shop = driver.find_element_by_xpath(
            "//ul[@class='gl-warp clearfix']/li[" + str(i) + "]//div[@class='p-shopnum']")
        hrefs.append(href)
        names.append(name.get_attribute("textContent").replace('\n', '').replace('\t', ''))#.replace('\n', '').replace('\t', '')
        prices.append(price.get_attribute("textContent").replace('\n', '').replace('\t', '').replace('￥',''))
        commits.append(commit.get_attribute("textContent").replace('\n', '').replace('\t', ''))
        shops.append(shop.get_attribute("textContent").replace('\n', '').replace('\t', ''))
    driver.find_element_by_xpath("//*[@id='J_bottomPage']/span[1]/a[9]").click()
    sleep(2)
    print("第"+str(j)+"页")
print("爬取完毕！")
#存数据

import pandas as pd
D = {"链接": hrefs,
     "名称": names,
     "价格": prices,
     "评价": commits,
     "商店": shops}
data = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in D.items()]))
print(data)
# 生成CSV文件
filename = "编程书籍-19.csv"
data.to_csv(filename, index=False,encoding='utf-8-sig')
print("关闭浏览器，保存数据")
