import os

# Bot settings
BOT_TOKEN = os.getenv("BOT_TOKEN", "8159106255:AAGUZ351bbLmgGTTkNIopb5RJDgW0QfbfaM")

# Data paths
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
SPELLS_FILE = os.path.join(DATA_DIR, "spells", "spells.json")
RULES_FILE = os.path.join(DATA_DIR, "rules", "rules.json")
CLASS_POWERS_FILE = os.path.join(DATA_DIR, "powers", "class_powers.json")
RACE_POWERS_FILE = os.path.join(DATA_DIR, "powers", "race_powers.json")
ORIGIN_POWERS_FILE = os.path.join(DATA_DIR, "powers", "origin_powers.json")
TORMENTA_POWERS_FILE = os.path.join(DATA_DIR, "powers", "tormenta_powers.json")
COMBAT_POWERS_FILE = os.path.join(DATA_DIR, "powers", "combat_powers.json")
DESTINY_POWERS_FILE = os.path.join(DATA_DIR, "powers", "destiny_powers.json")
MAGIC_POWERS_FILE = os.path.join(DATA_DIR, "powers", "magic_powers.json")
GRANTED_POWERS_FILE = os.path.join(DATA_DIR, "powers", "granted_powers.json")
GROUP_POWERS_FILE = os.path.join(DATA_DIR, "powers", "group_powers.json")

# Logging settings
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
