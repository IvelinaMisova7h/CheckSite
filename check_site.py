import requests

sites_to_check = ["https://google.com", "https://github.com", "https://wordpress.com"]

for site in sites_to_check:
    try:
        # Задаваме timeout=5, за да не увисва скриптът, ако сайтът не отговаря
        response = requests.get(site, timeout=5)

        if response.status_code == 200:
            print(f"✅ {site} работи перфектно!")
        else:
            print(f"⚠️ {site} върна проблем! Статус код: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print(f"❌ {site} е напълно паднал! (Грешка при свързването)")

    except requests.exceptions.Timeout:
        print(f"⏱️ {site} се забави твърде много! (Timeout)")

    except requests.exceptions.RequestException as e:
        print(f"🚨 Възникна неочаквана грешка с requests за {site}: {e}")
