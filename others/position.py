import pyautogui
import time 

time.sleep(5)
print(pyautogui.position())

# setor
# Point(x=1470, y=329)




#ti indeed
#Point(x=989, y=694)




# aplicar filtro
# Point(x=1198, y=826)














# # Rola até o final da página para forçar o carregamento de mais elementos (importante em sites com lazy loading).
# navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)

# elementos = navegador.find_elements(By.XPATH, '//a[contains(@href, "/vaga-de-")]')
# for el in elementos:
#     href = el.get_attribute("href")
#     if href and "infojobs.com.br/vaga-de" in href:
#         VAGAS.append(href)

# df = pd.DataFrame(VAGAS, columns=["Link"])
# df.drop_duplicates(subset="Link", inplace=True)
# df.to_excel("vagas_infojobs.xlsx", index=False)









#a final ta sempre sendo a segunda coordenada 

#print(pyautogui.position()) - pega a poscao do mause
#area = x=915, y=282 / x=908, y=329
# TI = x=821, y=619 / x=823, y=669
#aplicar filtro = x=1002, y=873 / (x=996, y=926) # area


#senoridade = x=1281, y=274  / 1294, y=322
# estagio = x=392, y=339 / x=392, y=391
#trainee = x=389, y=497 / x=396, y=556
#aplicar filtro = x=1004, y=581 / x=988, y=631
