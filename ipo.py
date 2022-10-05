from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('prefs', {
"download.default_directory": "D:\Projects\scraps\ipo_data", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})

from PyPDF2 import PdfMerger
from PyPDF2 import PdfFileWriter as w
import glob
import os


driver = webdriver.Chrome('D:\Projects\scraps\chromedriver_win32\chromedriver.exe', options=options)  # Optional argument, if not specified will search path.
query = 'https://search.ipindia.gov.in/IPOJournal/Journal/Patent'

driver.get(query)
time.sleep(3) # Let the user actually see something!
#html = driver.page_source
#soup = bs(html, "html.parser")

#rows = soup.find_all('tr')
#print(len(rows))
#print(rows[1].find_all('td')[:-1])
#buttons = soup.find_all('button')
#print(len(buttons))
#print(buttons[0])
for i in range(48):

    rows = driver.find_elements(By.TAG_NAME, 'tr')
    #for i in rows:
    #    e_html = i.get_attribute('innerHTML')
    dr = "D:\Projects\scraps\IPO\ipo_data"
    for row in rows[1:]:
        buttons = row.find_elements(By.TAG_NAME,'form')
        
        for button in buttons:
            button.click()
        pdf=w()
        file=open('D:\\Projects\\scraps\\IPO\\ipo_data\\ViewJournal_ex.pdf',"wb")
        for i in range(5):
            pdf.addBlankPage(219,297) #a4 size dimensions
        pdf.write(file)
        file.close()
        time.sleep(30)
        print(len(buttons))
        pdf_list = glob.glob(os.path.join(dr,"ViewJournal*.pdf"))
        issue = row.find_elements(By.TAG_NAME,'td')
        merger = PdfMerger()
        for pdf in pdf_list:
            #pdf=PdfFileWriter()
            #file=open(issue[1].text + ".txt","w")
            #pdf.write(file)
            #file.close()
            
            merger.append(pdf)
        merger.write("D:\Projects\scraps\IPO\ipo_data\ViewJournal_ex.pdf")
        merger.close()
        name = issue[1].text.split('/')
        rename_ = 'D:\\Projects\\scraps\\IPO\\ipo_data\\ '.strip()+ name[1][:4] + '_' + name[0] + ".pdf"
        os.rename("D:\\Projects\\scraps\\IPO\\ipo_data\\ViewJournal_ex.pdf", rename_)
        for pdf in glob.glob(os.path.join(dr,"ViewJournal*.pdf")):
            os.remove(pdf)

    next = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/div/div[1]/div/div/div[3]/div[2]/div/ul/li[10]/a').click()




time.sleep(10)
print('slept')
#driver.quit()