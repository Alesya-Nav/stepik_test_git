from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

link = "https://stepik.org/lesson/236895/step/1"
answer = math.log(int(time.time()))

# def login(browser):
#     browser.get(link)


@pytest.mark.parametrize("links", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
] )


def test_go_to_browser(browser, links):
    answer1 = math.log(int(time.time()))
    browser.get(links)

    # Ожидаем, пока элемент станет кликабельным и нажимаем
    try:
        message=""
        
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'stepik-loader__icon'))
        )
        
        button_enter = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "ember471"))
        )
        button_enter.click()

        button_field_login = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, 'id_login_email'))
        )
        button_field_login.send_keys("ale-sya-2003@mail.ru")

        button_field_password = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, 'id_login_password'))
        )
        button_field_password.send_keys("12345678+")

        button_submit = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login_form"]/button'))
        )
        button_submit.click()

        textarea_answer = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea"))
        )
        textarea_answer.clear()
        textarea_answer.send_keys(answer)

        button_submit_2 = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button_submit_2.click()


        answer_comp = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        feedback_text = answer_comp.text.strip() # получаем текст фидбека и убираем лишние пробелы
        print(feedback_text)
        
        assert(feedback_text)=="Correct!",f"Expected 'Correct!', but got {feedback_text}"
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")
    

    finally:
        print(answer)
        print(answer1)
        browser.quit()