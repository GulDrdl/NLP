from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)


file = open("ilk.txt", "w", encoding="utf-8")
file.close()

driver.get("https://www.trendyol.com/harley-davidson/kadin-siyah-cizme-p-1263583/yorumlar?boutiqueId=618697&merchantId=195806")


time.sleep(3)



for i in range(1, 3500):
    uni_path = f"/html/body/div[1]/div[3]/div/div/div/div/div[3]/div/div/div[3]/div[2]/div[{i}]/div[2]/p"

    try:
        # By.XPATH ile find_element kullanın
        uni_name = driver.find_element(By.XPATH, uni_path).text

        with open("ilk.txt", "a", encoding="utf-8") as f:

         f.write(f"\n('{i} - {uni_name}  . ')")
         driver.execute_script("window.scrollTo(0,document.body.scrollHeight-1500)")

        print(uni_name)




    except Exception as e:
        print(f"{i}. veri alınırken hata oluştu: {e}")

driver.quit()


