from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("character", choices = ['guile', 'marisa', 'rashid', 'lily', 'cammy', 'zangief', 'jp', 'marisa', 'manon', 'deejay', 'honda', 'dhalsim', 'blanka', 'ken', 'juri', 'kimberly', 'chunli', 'jamie', 'luke', 'ryu'], help="input your character")
# parser.add_argument("input", help="which move do you want from the character?")
move = parser.parse_args()

driver = webdriver.Edge()
driver.get(f"https://www.streetfighter.com/6/character/{move.character}/frame")


move_list = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr:not([class])')
TABLE_COLUMN = 15


moves_dict = {}

for move in move_list:
    
    colunas = move.find_elements(By.TAG_NAME, "td")
    nome_do_move = colunas[0].find_element(By.TAG_NAME, "span").get_attribute("innerText")
    startup = colunas[1].get_attribute("innerText")
    active = colunas[2].get_attribute("innerText")
    recovery = colunas[3].get_attribute("innerText")
    oh = colunas[4].get_attribute("innerText")
    ob = colunas[5].get_attribute("innerText")
    cancel = colunas[6].get_attribute("innerText")
    damage = colunas[7].get_attribute("innerText")
    scaling = colunas[8].get_attribute("innerText") 
    drive_increase = colunas[9].get_attribute("innerText") 
    drive_decrease = colunas[10].get_attribute("innerText") 
    drive_decrease_pc = colunas[11].get_attribute("innerText") 
    sa_increase = colunas[12].get_attribute("innerText") 
    high_low = colunas[13].get_attribute("innerText") 
    misc = colunas[14].get_attribute("innerText") 


    moves_dict[nome_do_move] = {
        "startup" : startup,
        "active" : active,
        "recovery" : recovery,
        "oh" : oh,
        "ob" : startup,
        "cancel" : cancel,
        "damage" : damage,
        "scaling" : scaling,
        "drive_increase" : drive_increase,
        "drive_decrease" : drive_decrease,
        "drive_decrease_pc" : drive_decrease_pc,
        "sa_increase" : sa_increase,
        "high_low" : high_low,
        "misc" : misc
    }


for key, value in moves_dict.items():
    print(f"{key}:{value}")

# moves_name = driver.find_elements(By.CLASS_NAME, "frame_arts__CNftl")
# moves_startup = driver.find_elements(By.CLASS_NAME, "frame_startup_frame__IeKL6")
# moves_active = driver.find_elements(By.CLASS_NAME, "frame_active_frame__1pLtR")
# moves_recovery = driver.find_elements(By.CLASS_NAME, "frame_recovery_frame__WLqFt")
# move_list = {move.get_attribute("innerText"): {"Startup": startup.get_attribute("innerText"), "Active": active.get_attribute("innerText"), "Recovery": recovery.get_attribute("innerText")}
#              for move in moves_name
#              for startup in moves_startup
#              if moves_name.index(move)+1 == moves_startup.index(startup)
#              for active in moves_active
#              if moves_name.index(move)+1 == moves_active.index(active)
#              for recovery in moves_recovery
#              if moves_name.index(move)+1 == moves_recovery.index(recovery)}
# for data,key in move_list[move.input].items():
#     print(f"{data}: {key}")