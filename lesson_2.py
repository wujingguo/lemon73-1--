

dict_1={"class_id":45,"num":20}
num=dict_1["num"]
if num > 5:
    print("班级上课人数:{}".format(num))
else:
    print("上课人数不足5人")
list3=["方方土","七木","荷花鱼","kingo","Amiee","焕蓝"]
list4=[]
list2=[18,19,20,21,22,23]
list1=["female","man","female","man","female","man"]
list5=["北京","深圳","南京","上海","安徽","杭州"]
for i in range(0,6,1):
    dict1=dict(name=list3[i],age=list2[i],sex=list1[i],city=list5[i])
    list4.append(dict1)
print(list4)
str1="问问","青青","haha","123455","dog"
list1=list(str1)
print(list1)
count=0
for i in range(10):
    count+=i
print(count)
def hanshu_1 (list1,dict1,str1):
    list2=list(dict1)
    sum1=len(list1)+len(str1)+len(list2)
    hanshu_1=sum1
    return hanshu_1
hanshu_1([1,2,3],'"nihao","中国"',{"name":"静静"})
hanshu_1()
if sum1 > 5:
    print("True")
else:
    print("False")
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待10秒，最多等待10秒
driver.get("http://120.78.128.25:8765")
driver.maximize_window()
driver.get("http://erp.lemfix.com")
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()
driver.find_element_by_xpath('//input[@id="username"]').send_keys("test123")
driver.find_element_by_xpath('//input[@name="password"]').send_keys("123456")
driver.find_element_by_xpath('//button[@id="btnSubmit"]').click()
page_text=driver.find_element_by_xpath('//div[@class="login-logo"]//b').text
# print(page_text)
driver.find_element_by_xpath('//b[text()="柠檬ERP"]')
if page_text == "柠檬ERP":
    print("这个页面的标题是:{}".format(page_text))
else:
    print("这个条件测试用例不通过！")
# time.sleep(4)
page_text=driver.title
print("这个页面的标题是:{}".format(page_text))
login_user=driver.find_element_by_xpath('//p[text()="测试用户"]').text
if login_user == "测试用户":
    print("这个登录的用户名是:{}".format(login_user))
else:
    print("这个条件测试用例不通过！")
driver.find_element_by_xpath('//span[text()="零售出库"]').click()

#driver.find_element_by_xpath('//iframe[@id="tabpanel-adbd3de9dd-frame"]').send_keys("321")
def function_len(object):
    # if type(object)==str or type(object)==list or type(object)==dict:
    if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):
        leng=len(object)
        if leng >5:
            print('True')
        else:
            print('False')
    else:
        print("这个数据类型存在问题！")
function_len((1,2,3,4))

