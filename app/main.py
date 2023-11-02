from playwright.sync_api import sync_playwright
import tkinter as tk
from tkinter import messagebox

class RouterConfig:
    def __init__(self):
        self.admin_router_page = "http://192.168.1.1/admin/login.asp"
        self.browser = ""
        self.page = ""

    def runActions(self):
         with sync_playwright() as p:
            try:
                browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                self.browser =  p.chromium.launch(executable_path = browser_path, headless=False)
                self.page =  self.browser.new_page()

                self.page.goto(f"{self.admin_router_page}")

                self.page.fill('//*[@id="username"]', "admin")
                self.page.fill('//*[@id="password"]', "Utopia@26")
                self.page.locator('input:has-text("Login")').click()
                self.page.locator('//*[@id="nav"]/li[3]/a').click()

                self.page.wait_for_selector('//iframe[@id="contentIframe"]')
                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('//input[@name="ssid"]').fill("gui-teste-loja")
                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('input[name="save"][value="Apply Changes"]').click()

                self.page.locator('//*[@id="side"]/li[1]/ul/li[3]/a').click()
                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('//input[@id="wpapsk"]').fill("12345678")
                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('input[name="save"][value="Apply Changes"]').click()

                self.page.locator('//*[@id="side"]/li[2]/h3/a').click()
                self.page.wait_for_selector('//iframe[@id="contentIframe"]')
                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('//input[@name="ssid"]').fill("gui-teste-loja")
                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('input[name="save"][value="Apply Changes"]').click()


                self.page.locator('//*[@id="side"]/li[2]/ul/li[3]/a').click()
                self.page.wait_for_selector('//iframe[@id="contentIframe"]')
                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('//input[@id="wpapsk"]').fill("12345678")
                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('input[name="save"][value="Apply Changes"]').click()

                self.page.locator('//*[@id="nav"]/li[4]/a').click()
                self.page.wait_for_selector('//iframe[@id="contentIframe"]')
                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('//input[@name="vid"]').fill("4005")
    
                self.page.wait_for_selector('//iframe[@id="contentIframe"]')
                self.page.evaluate('window.scrollBy(0,900)')

                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('//input[@name="pppUserName"]').fill("gui-teste-loja")
                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('//input[@name="pppPassword"]').fill("gui")

                checkbox_LAN_1 = self.page.frame_locator('//iframe[@id="contentIframe"]').locator('//*[@id="tbl_pmap"]/tbody/tr[2]/td[1]/input')
                checkbox_LAN_2 = self.page.frame_locator('//iframe[@id="contentIframe"]').locator('//*[@id="tbl_pmap"]/tbody/tr[2]/td[2]/input')
                is_checked_1 = checkbox_LAN_1.is_checked()
                is_checked_2 = checkbox_LAN_2.is_checked()

                if not is_checked_1:
                    checkbox_LAN_1.click()
                if not is_checked_2:
                    checkbox_LAN_2.click()
                else:
                    pass

                self.page.frame_locator('//iframe[@id="contentIframe"]').locator('//input[@name="apply"]').click()
                self.page.locator('input[name="save"]').click()
                self.page.wait_for_load_state('load')

            except Exception as error:
                root = tk.Tk()
                root.withdraw()
                root.lift()

                messagebox.showerror("ERROR!", str(error))

                root.destroy()

            finally:
                root = tk.Tk()
                root.withdraw()

                self.browser.close()

                root.lift()
                messagebox.showinfo("SHORELINE SH1030W CONFIGURATION COMPLETED!", str('''
CONFIG CHANGED:

5G SSID: gui-teste-loja
5G PASSWORD: 12345678
                                                                                 
2.4G SSID: gui-teste-loja
2.4G PASSWORD: 12345678
VLAN: 4005
                                                                              
PPPoE Username: gui-teste-loja
PPPoE Password: gui
                                                                              
LAN_1: OK
LAN_2: OK '''))
                
if __name__ == "__main__":
    config = RouterConfig()
    config.runActions()