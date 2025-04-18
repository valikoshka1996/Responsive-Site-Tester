import tempfile
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import os
import shutil

sizes = {
    "mobile": (375, 812),
    "tablet": (768, 1024),
    "laptop": (1366, 768),
    "desktop": (1920, 1080)
}

def capture_screenshots(url, session_id):
    chromedriver_autoinstaller.install()
    
    options = Options()
    options.headless = True
    
    # Створюємо тимчасову директорію для кожного сеансу з унікальним ідентифікатором
    unique_dir_name = str(uuid.uuid4())  # Генеруємо унікальний ідентифікатор
    user_data_dir = tempfile.mkdtemp(prefix=unique_dir_name + "_")  # Унікальна директорія
    options.add_argument(f"user-data-dir={user_data_dir}")  # Вказуємо унікальний каталог для кожного запуску
    
    # Додаємо параметри для очищення сесії і уникнення залишкових даних
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    try:
        driver = webdriver.Chrome(options=options)

        # Ініціалізація порожнього словника для збереження шляхів до скріншотів
        paths = {}

        for device, size in sizes.items():
            driver.set_window_size(*size)
            driver.get(url)
            path = f'static/screenshots/{session_id}_{device}.png'
            driver.save_screenshot(path)
            paths[device] = path  # Збереження шляху до кожного скріншота

        driver.quit()
    except Exception as e:
        print(f"Error during the screenshot capture: {e}")
        return {}  # Повертаємо порожній словник у випадку помилки
    finally:
        # Видалення тимчасової директорії після завершення роботи
        try:
            shutil.rmtree(user_data_dir)  # Використовуємо shutil для видалення директорії
        except Exception as e:
            print(f"Error removing temporary directory: {e}")

    return paths
