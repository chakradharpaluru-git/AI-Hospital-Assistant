from pathlib import Path
from PIL import Image


# Get assets folder path
ASSETS_PATH = Path(__file__).parent.parent / "assets"


def get_image(image_name):

    image_path = ASSETS_PATH / image_name

    if image_path.exists():
        return Image.open(image_path)

    return None


# Images mapping

LOGO = get_image("logo.png")

HERO = get_image("hero.jpg")

HOSPITAL = get_image("hospital_bg.jpg")

DOCTOR = get_image("doctor.png")

REPORT = get_image("report.jpg")

CHATBOT = get_image("chatbot.jpg")

EMERGENCY = get_image("emergency.jpg")

INSURANCE = get_image("insurance.jpg")

APPOINTMENT = get_image("appointment.jpg")

DASHBOARD = get_image("dashboard_banner.jpg")