from pages.Imports import *
from pages.functions import *

# "https://www.kickstarter.com/discover/categories/art",
urls = [
    "https://www.kickstarter.com/discover/categories/art",
    "https://www.kickstarter.com/discover/categories/art/ceramics",
    "https://www.kickstarter.com/discover/categories/art/conceptual%20art",
    "https://www.kickstarter.com/discover/categories/art/digital%20art",
    "https://www.kickstarter.com/discover/categories/art/illustration",
    "https://www.kickstarter.com/discover/categories/art/installations",
    "https://www.kickstarter.com/discover/categories/art/mixed%20media",
    "https://www.kickstarter.com/discover/categories/art/painting",
    "https://www.kickstarter.com/discover/categories/art/performance%20art",
    "https://www.kickstarter.com/discover/categories/art/public%20art",
    "https://www.kickstarter.com/discover/categories/art/sculpture",
    "https://www.kickstarter.com/discover/categories/art/social%20practice",
    "https://www.kickstarter.com/discover/categories/art/textiles",
    "https://www.kickstarter.com/discover/categories/art/video%20art",
    "https://www.kickstarter.com/discover/categories/comics",
    "https://www.kickstarter.com/discover/categories/comics/anthologies",
    "https://www.kickstarter.com/discover/categories/comics/comic%20books",
    "https://www.kickstarter.com/discover/categories/comics/events",
    "https://www.kickstarter.com/discover/categories/comics/graphic%20novels",
    "https://www.kickstarter.com/discover/categories/comics/webcomics",
    "https://www.kickstarter.com/discover/categories/crafts",
    "https://www.kickstarter.com/discover/categories/crafts/candles",
    "https://www.kickstarter.com/discover/categories/crafts/crochet",
    "https://www.kickstarter.com/discover/categories/crafts/diy",
    "https://www.kickstarter.com/discover/categories/crafts/embroidery",
    "https://www.kickstarter.com/discover/categories/crafts/glass",
    "https://www.kickstarter.com/discover/categories/crafts/knitting",
    "https://www.kickstarter.com/discover/categories/crafts/pottery",
    "https://www.kickstarter.com/discover/categories/crafts/printing",
    "https://www.kickstarter.com/discover/categories/crafts/quilts",
    "https://www.kickstarter.com/discover/categories/crafts/stationery",
    "https://www.kickstarter.com/discover/categories/crafts/weaving",
    "https://www.kickstarter.com/discover/categories/crafts/woodworking",
    "https://www.kickstarter.com/discover/categories/dance",
    "https://www.kickstarter.com/discover/categories/dance/performances",
    "https://www.kickstarter.com/discover/categories/dance/spaces",
    "https://www.kickstarter.com/discover/categories/dance/workshops",
    "https://www.kickstarter.com/discover/categories/design",
    "https://www.kickstarter.com/discover/categories/design/architecture",
    "https://www.kickstarter.com/discover/categories/design/civic%20design",
    "https://www.kickstarter.com/discover/categories/design/graphic%20design",
    "https://www.kickstarter.com/discover/categories/design/interactive%20design",
    "https://www.kickstarter.com/discover/categories/design/product%20design",
    "https://www.kickstarter.com/discover/categories/design/toys",
    "https://www.kickstarter.com/discover/categories/design/typography",
    "https://www.kickstarter.com/discover/categories/fashion",
    "https://www.kickstarter.com/discover/categories/fashion/accessories",
    "https://www.kickstarter.com/discover/categories/fashion/apparel",
    "https://www.kickstarter.com/discover/categories/fashion/childrenswear",
    "https://www.kickstarter.com/discover/categories/fashion/couture",
    "https://www.kickstarter.com/discover/categories/fashion/jewelry",
    "https://www.kickstarter.com/discover/categories/fashion/pet%20fashion",
    "https://www.kickstarter.com/discover/categories/fashion/ready-to-wear",
    "https://www.kickstarter.com/discover/categories/film%20&%20video",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/action",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/animation",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/comedy",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/documentary",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/drama",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/experimental",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/family",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/fantasy",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/festivals",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/horror",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/movie%20theaters",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/narrative%20film",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/romance",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/science%20fiction",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/shorts",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/television",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/thrillers",
    "https://www.kickstarter.com/discover/categories/film%20&%20video/webseries",
    "https://www.kickstarter.com/discover/categories/food",
    "https://www.kickstarter.com/discover/categories/food/community%20gardens",
    "https://www.kickstarter.com/discover/categories/food/cookbooks",
    "https://www.kickstarter.com/discover/categories/food/drinks",
    "https://www.kickstarter.com/discover/categories/food/events",
    "https://www.kickstarter.com/discover/categories/food/farmer's%20markets",
    "https://www.kickstarter.com/discover/categories/food/farms",
    "https://www.kickstarter.com/discover/categories/food/food%20trucks",
    "https://www.kickstarter.com/discover/categories/food/restaurants",
    "https://www.kickstarter.com/discover/categories/food/small%20batch",
    "https://www.kickstarter.com/discover/categories/food/spaces",
    "https://www.kickstarter.com/discover/categories/food/vegan",
    "https://www.kickstarter.com/discover/categories/games",
    "https://www.kickstarter.com/discover/categories/games/gaming%20hardware",
    "https://www.kickstarter.com/discover/categories/games/live%20games",
    "https://www.kickstarter.com/discover/categories/games/mobile%20games",
    "https://www.kickstarter.com/discover/categories/games/playing%20cards",
    "https://www.kickstarter.com/discover/categories/games/puzzles",
    "https://www.kickstarter.com/discover/categories/games/tabletop%20games",
    "https://www.kickstarter.com/discover/categories/games/video%20games",
    "https://www.kickstarter.com/discover/categories/journalism",
    "https://www.kickstarter.com/discover/categories/journalism/audio",
    "https://www.kickstarter.com/discover/categories/journalism/photo",
    "https://www.kickstarter.com/discover/categories/journalism/print",
    "https://www.kickstarter.com/discover/categories/journalism/video",
    "https://www.kickstarter.com/discover/categories/journalism/web",
    "https://www.kickstarter.com/discover/categories/music",
    "https://www.kickstarter.com/discover/categories/music/chiptune",
    "https://www.kickstarter.com/discover/categories/music/classical%20music",
    "https://www.kickstarter.com/discover/categories/music/comedy",
    "https://www.kickstarter.com/discover/categories/music/country%20&%20folk",
    "https://www.kickstarter.com/discover/categories/music/electronic%20music",
    "https://www.kickstarter.com/discover/categories/music/faith",
    "https://www.kickstarter.com/discover/categories/music/hip-hop",
    "https://www.kickstarter.com/discover/categories/music/indie%20rock",
    "https://www.kickstarter.com/discover/categories/music/jazz",
    "https://www.kickstarter.com/discover/categories/music/kids",
    "https://www.kickstarter.com/discover/categories/music/metal",
    "https://www.kickstarter.com/discover/categories/music/pop",
    "https://www.kickstarter.com/discover/categories/music/punk",
    "https://www.kickstarter.com/discover/categories/music/r&b",
    "https://www.kickstarter.com/discover/categories/music/rock",
    "https://www.kickstarter.com/discover/categories/music/world%20music",
    "https://www.kickstarter.com/discover/categories/photography",
    "https://www.kickstarter.com/discover/categories/photography/animals",
    "https://www.kickstarter.com/discover/categories/photography/fine%20art",
    "https://www.kickstarter.com/discover/categories/photography/nature",
    "https://www.kickstarter.com/discover/categories/photography/people",
    "https://www.kickstarter.com/discover/categories/photography/photobooks",
    "https://www.kickstarter.com/discover/categories/photography/places",
    "https://www.kickstarter.com/discover/categories/publishing",
    "https://www.kickstarter.com/discover/categories/publishing/academic",
    "https://www.kickstarter.com/discover/categories/publishing/anthologies",
    "https://www.kickstarter.com/discover/categories/publishing/art%20books",
    "https://www.kickstarter.com/discover/categories/publishing/calendars",
    "https://www.kickstarter.com/discover/categories/publishing/children's%20books",
    "https://www.kickstarter.com/discover/categories/publishing/comedy",
    "https://www.kickstarter.com/discover/categories/publishing/fiction",
    "https://www.kickstarter.com/discover/categories/publishing/literary%20journals",
    "https://www.kickstarter.com/discover/categories/publishing/literary%20spaces",
    "https://www.kickstarter.com/discover/categories/publishing/nonfiction",
    "https://www.kickstarter.com/discover/categories/publishing/periodicals",
    "https://www.kickstarter.com/discover/categories/publishing/poetry",
    "https://www.kickstarter.com/discover/categories/publishing/radio%20&%20podcasts",
    "https://www.kickstarter.com/discover/categories/publishing/translations",
    "https://www.kickstarter.com/discover/categories/publishing/young%20adult",
    "https://www.kickstarter.com/discover/categories/publishing/zines",
    "https://www.kickstarter.com/discover/categories/technology",
    "https://www.kickstarter.com/discover/categories/technology/3d%20printing",
    "https://www.kickstarter.com/discover/categories/technology/apps",
    "https://www.kickstarter.com/discover/categories/technology/camera%20equipment",
    "https://www.kickstarter.com/discover/categories/technology/diy%20electronics",
    "https://www.kickstarter.com/discover/categories/technology/fabrication%20tools",
    "https://www.kickstarter.com/discover/categories/technology/flight",
    "https://www.kickstarter.com/discover/categories/technology/gadgets",
    "https://www.kickstarter.com/discover/categories/technology/hardware",
    "https://www.kickstarter.com/discover/categories/technology/makerspaces",
    "https://www.kickstarter.com/discover/categories/technology/robots",
    "https://www.kickstarter.com/discover/categories/technology/software",
    "https://www.kickstarter.com/discover/categories/technology/sound",
    "https://www.kickstarter.com/discover/categories/technology/space%20exploration",
    "https://www.kickstarter.com/discover/categories/technology/wearables",
    "https://www.kickstarter.com/discover/categories/technology/web",
    "https://www.kickstarter.com/discover/categories/theater",
    "https://www.kickstarter.com/discover/categories/theater/comedy",
    "https://www.kickstarter.com/discover/categories/theater/experimental",
    "https://www.kickstarter.com/discover/categories/theater/festivals",
    "https://www.kickstarter.com/discover/categories/theater/immersive",
    "https://www.kickstarter.com/discover/categories/theater/musical",
    "https://www.kickstarter.com/discover/categories/theater/plays",
    "https://www.kickstarter.com/discover/categories/theater/spaces",
    "https://www.kickstarter.com/discover",
    "https://www.kickstarter.com/discover/tags/accessible-art",
    "https://www.kickstarter.com/discover/tags/ride-with-it",
    "https://www.kickstarter.com/discover/tags/diy",
    "https://www.kickstarter.com/discover/tags/go-green",
    "https://www.kickstarter.com/discover/tags/kids",
    "https://www.kickstarter.com/discover/tags/lgbtq",
    "https://www.kickstarter.com/discover/tags/magic",
    "https://www.kickstarter.com/discover/tags/public-benefit",
    "https://www.kickstarter.com/discover/tags/robots",
    "https://www.kickstarter.com/discover/tags/rpg",
    "https://www.kickstarter.com/discover/tags/sci-fi",
    "https://www.kickstarter.com/discover/tags/stem",
    "https://www.kickstarter.com/discover/tags/heartstrings-and-hardbacks",
    "https://www.kickstarter.com/discover/tags/long-story-short",
    "https://www.kickstarter.com/discover/tags/make-100",
    "https://www.kickstarter.com/discover/tags/witchstarter",
    "https://www.kickstarter.com/discover/tags/zine-quest",
    "https://www.kickstarter.com/discover/tags/spotlight-on-aanhpi-creators",
    "https://www.kickstarter.com/discover/tags/spotlight-on-black-creators",
    "https://www.kickstarter.com/discover/tags/spotlight-on-hispanic-creators",
    "https://www.kickstarter.com/discover/tags/spotlight-on-lgbtqia-creators",
    "https://www.kickstarter.com/discover/tags/womens-history-month"
]
# urls = [
#     "https://www.kickstarter.com/discover/categories/comics",
#     "https://www.kickstarter.com/discover/categories/crafts",
#     "https://www.kickstarter.com/discover/categories/dance",
#     "https://www.kickstarter.com/discover/categories/design",
#     "https://www.kickstarter.com/discover/categories/fashion",
#     "https://www.kickstarter.com/discover/categories/film%20&%20video",
#     "https://www.kickstarter.com/discover/categories/food",
#     "https://www.kickstarter.com/discover/categories/games",
#     "https://www.kickstarter.com/discover/categories/journalism",
#     "https://www.kickstarter.com/discover/categories/music",
#     "https://www.kickstarter.com/discover/categories/photography",
#     "https://www.kickstarter.com/discover/categories/publishing",
#     "https://www.kickstarter.com/discover/categories/technology",
#     "https://www.kickstarter.com/discover/categories/theater"
# ]


def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = "w" if new else "a"
    with open(filename, mode, newline="", encoding='utf-8') as f:
        f.writelines(data)

def main_code_1():
    try:
        driver = get_undetected_chrome_browser('christoph')
        time.sleep(1)
        driver.get("https://google.com/")
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
        for url in urls:
            try:
                driver.get(url)
                # driver.get("https://www.kickstarter.com/discover")
                time.sleep(1)        
                try:
                    side_modall = HomePage(driver)
                    side_modall.wait(ProfileResources.side_modal)
                    time.sleep(2)
                    side_modal_crosss = HomePage(driver)
                    side_modal_crosss.click_btn(ProfileResources.side_modal_cross)
                except:
                    pass
                project_card_xpath = ProfileResources.project_url
                load_more_button_xpath = ProfileResources.load_more_btn
                try:
                    # Main scraping loop
                    while True:
                        # Find all project cards
                        project_cards = driver.find_elements(By.XPATH, project_card_xpath)
                        for card in project_cards:
                            project_url = card.get_attribute('href')
                            if not is_url_in_csv(project_url, csv_file):
                                print(project_url)
                                save_url_to_csv(project_url, csv_file)
                            
                        # Try to click the 'Load More' button
                        try:
                            time.sleep(2)
                            load_more_button = driver.find_element(By.XPATH, load_more_button_xpath)
                            time.sleep(5)
                            ActionChains(driver).move_to_element(load_more_button).perform()
                            time.sleep(5)
                            load_more_button.click()
                            try:
                                current_url = driver.current_url
                                if "page=200" in current_url:
                                    print("page 200 reached")
                                    print("=====================================")
                                    print(url)
                                    print("=====================================")
                                    break
                            except:
                                print("loading")
                            time.sleep(30)
                        except NoSuchElementException:
                            crruent_url = driver.current_url
                            print("No more 'Load More' button found or end of the list reached.")
                            print(driver.current_url)
                            break
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
    # Close the browser
    driver.quit()

print("Scraping complete. Data saved to CSV.")
    
    
    
    
  