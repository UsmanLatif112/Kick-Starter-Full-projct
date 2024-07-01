from pages.Imports import *
from pages.functions import *

def main_code_message_sending():
    # csv_file_path = 'D:\\my\\New folder\\kick starter\\kickstarter_1800.csv'
    csv_file_path = 'C:\\Users\\Administrator\\Desktop\\project\\Kick_Starter_Full_projct\\Messages_Script\\kickstarter_1800.csv'
    # csv_file_path = 'C:\\Users\\Administrator\\Desktop\\New_folder\\kick-starter\\kickstarter_projects.csv'
    
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        counter = 0
        for row in reader:
            try:
                Project_Urls = row[0]
                if not is_url_in_csvv(Project_Urls, csv_filee):
                    print("Url not found in error message csv")
                if not is_url_in_csvv_error(Project_Urls, csv_filee_error):
                    print("Url not found in Sent message csv")
                    driver = get_undetected_chrome_browser('christoph')
                    driver.maximize_window()
                    driver.get("https://www.google.com/")
                    time.sleep(2)
                    try:
                        Search_barr = HomePage(driver)
                        Search_barr.click_btn(MessageResources.Search_bar)
                        time.sleep(2)
                        Search_bar_r = HomePage(driver)
                        keywordss = random.choice(keywords)
                        Search_bar_r.enter_name_delay(MessageResources.Search_bar, keywordss)
                        time.sleep(2)
                        ActionChains(driver).send_keys(Keys.ENTER).perform()
                    except:
                        print(f"searxh bar not found {Project_Urls}")
                        
                    gentle_human_like_scroll(driver, duration=8)
                    time.sleep(7)
                    random_mouse_movemen_t(5)
                    time.sleep(7)
                    website = random.choice(websites)
                    time.sleep(7)
                    driver.get(website)
                    time.sleep(7)
                    gentle_human_like_scroll(driver, duration=8)
                    time.sleep(7)
                    random_mouse_movemen_t(5)
                    time.sleep(7)
                    print(Project_Urls)
                    time.sleep(7)
                    driver.get(f"{Project_Urls}")
                    time.sleep(7) 
                    try:
                        side_modall = HomePage(driver)
                        side_modall.wait(ProfileResources.side_modal)
                        side_modal_crosss = HomePage(driver)
                        side_modal_crosss.click_btn(ProfileResources.side_modal_cross)
                    except:
                        print(f"Side modal not found {Project_Urls}")
                    time.sleep(5)
                    gentle_human_like_scroll(driver, duration=8)
                    time.sleep(5)
                    random_mouse_movemen_t(5)
                    time.sleep(5)
                    try:
                        see_more_e = driver.find_element(By.XPATH,'//*[@id="content-wrap"]//*[@class="NS_projects__description_section m-auto"]//*[@class="col col-4 js-rewards-column max-w62 sticky-rewards"]//*[@class="pl1"][contains(normalize-space(), "See more")]')
                        time.sleep(10)
                        if see_more_e:
                            try:
                                print("See more button found")
                                time.sleep(10)
                                ActionChains(driver).move_to_element(see_more_e).perform()
                                time.sleep(5)
                                see_more_e_e = HomePage(driver)
                                see_more_e_e.click_btn(MessageResources.See_More_btn)
                                try:
                                    modal_cancel_1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content-wrap"]//*[@class="shadow-low p4 max-h70vh auto-scroll-y clip"][contains(normalize-space(), "About the creator")]',)))
                                    if modal_cancel_1:
                                        Contact_me = driver.find_element(By.XPATH,'//*[@id="content-wrap"]//*[@class="shadow-low p4 max-h70vh auto-scroll-y clip"]//button[contains(normalize-space(), "Contact me")]')
                                        time.sleep(5)
                                        ActionChains(driver).move_to_element(Contact_me).perform()
                                        time.sleep(5)
                                        Contact_me.click()
                                        time.sleep(5)
                                        try:
                                            Message_feild = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content-wrap"]//*[@class="shadow-low p4 max-h70vh auto-scroll-y clip"]//textarea[@placeholder="Type your message here"]',)))
                                            if Message_feild:
                                                Message_feild.click()
                                                time.sleep(5)
                                                Message_feild_d = HomePage(driver)
                                                messages = random.choice(messagess)
                                                Message_feild_d.enter_name_delay(MessageResources.Message_feild_dd, messages)
                                                time.sleep(5)
                                                try:
                                                    Send_message = driver.find_element(By.XPATH,'//*[@id="content-wrap"]//*[@class="shadow-low p4 max-h70vh auto-scroll-y clip"]//button[contains(normalize-space(), "Send Message")]')
                                                    time.sleep(5)
                                                    ActionChains(driver).move_to_element(Send_message).perform()
                                                    time.sleep(5)
                                                    Send_message.click()
                                                except:
                                                    print(f"Sent messagebuton not found {Project_Urls}")
                                                try:
                                                    Message_sent_pop = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@class="jGrowl-message"][contains(normalize-space(), "Your message has been sent!")]',)))
                                                    if Message_sent_pop:
                                                        print(f"Message sent {Project_Urls}")
                                                    save_url_to_csvv (Project_Urls, csv_filee)
                                                except:
                                                    print(f"message not sent {Project_Urls}") 
                                                    save_url_to_csvv_v (Project_Urls, csv_filee_e)    
                                        except:
                                            print(f"error in message typing {Project_Urls}")
                                except:
                                    print(f"message modal not found {Project_Urls}")
                                    save_url_to_csvv_v (Project_Urls, csv_filee_e)
                                time.sleep(30)
                                websitee = random.choice(websites)
                                driver.get(websitee)
                                time.sleep(5)
                                gentle_human_like_scroll(driver, duration=8)
                                time.sleep(5)
                                random_mouse_movemen_t(5)
                                time.sleep(5)
                                driver.quit()
                                kill_chrome_processes()
                                counter += 1  # Increment the counter
                                print(counter)
                                time.sleep(180)
                                if counter % 20 == 0:
                                    print("Waiting for 2 hours...")
                                    time.sleep(7200)  # Wait for 1 hour (3600 seconds)
                                    counter = 0
                                    break
                            except:
                                print(f"see more button not found {Project_Urls}")
                                save_url_to_csvv_v (Project_Urls, csv_filee_e)
                                driver.quit()
                                kill_chrome_processes()
                                time.sleep(120)
                            
                        else:
                            print(f"see more button not found {Project_Urls}")
                            save_url_to_csvv_v (Project_Urls, csv_filee_e)
                            driver.quit()
                            kill_chrome_processes()
                            time.sleep(120)
                    except:
                        print(f"see more button not found {Project_Urls}")
                        save_url_to_csvv_v (Project_Urls, csv_filee_e)
                        driver.quit()
                        kill_chrome_processes() 
                        time.sleep(120) 
            except Exception as e:
                print(e)
                print(f"Error sensing message {Project_Urls}")
                save_url_to_csvv_v (Project_Urls, csv_filee_e)
                driver.quit()
                kill_chrome_processes()
                time.sleep(120)
