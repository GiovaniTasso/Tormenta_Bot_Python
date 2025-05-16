from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from typing import List, Dict, Any
from ..domain.models import Spell


def create_main_menu_keyboard() -> InlineKeyboardMarkup:
    """Create the main menu keyboard with centered buttons and emojis."""
    keyboard = [
        [InlineKeyboardButton("✨ Magias ", callback_data="magias_menu")],
        [InlineKeyboardButton("📖 Regras ", callback_data="regras_menu")],
        [InlineKeyboardButton("⚡ Poderes ", callback_data="poderes_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)

def create_magias_menu_keyboard() -> InlineKeyboardMarkup:
    """Create the magias (spells) menu keyboard."""
    keyboard = [
        [InlineKeyboardButton("✨ Buscar Magias ", callback_data="search_spells")],
        [InlineKeyboardButton("📜 Listar Magias ", callback_data="list_magias_options")],
        [InlineKeyboardButton("↩️ Voltar  ", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

def create_regras_menu_keyboard() -> InlineKeyboardMarkup:
    """Create the regras (rules) menu keyboard."""
    keyboard = [
        [InlineKeyboardButton("📖 Buscar Regras ", callback_data="rules")],
        [InlineKeyboardButton("📜 Listar Regras ", callback_data="list_rules")],
        [InlineKeyboardButton("↩️ Voltar ", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

def create_poderes_menu_keyboard() -> InlineKeyboardMarkup:
    """Create the poderes (powers) menu keyboard."""
    keyboard = [
        [InlineKeyboardButton("💪 Combate ", callback_data="powers_combate")],
        [InlineKeyboardButton("🌠 Destino ", callback_data="powers_destino")],
        [InlineKeyboardButton("🧙‍♂️ Magia ", callback_data="powers_magia")],
        [InlineKeyboardButton("🛐 Concedidas ", callback_data="powers_concedidas")],
        [InlineKeyboardButton("👹 Tormenta ", callback_data="powers_tormenta")],
        [InlineKeyboardButton("👥 Grupo ", callback_data="powers_grupo")],
        [InlineKeyboardButton("🧝 Raça ", callback_data="powers_race_list")],
        [InlineKeyboardButton("🏹 Classe ", callback_data="powers_class_list")],
        [InlineKeyboardButton("↩️ Voltar ", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

def create_list_magias_options_keyboard() -> InlineKeyboardMarkup:
    """Create a keyboard for selecting how to list spells."""
    keyboard = [
        [InlineKeyboardButton("✨ Por Tipo ", callback_data="list_spells_by_type")],
        [InlineKeyboardButton("🏆 Por Nível ", callback_data="list_spells")],
        [InlineKeyboardButton("↩️ Voltar ️", callback_data="magias_menu")],
        [InlineKeyboardButton("📋 Voltar ao Menu Principal ", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

def create_powers_menu_keyboard() -> InlineKeyboardMarkup:
    """Create the powers search menu keyboard."""
    keyboard = [
        [InlineKeyboardButton("⚔️ Poderes de Classe", callback_data="powers_class")],
        [InlineKeyboardButton("🧟 Poderes de Raça", callback_data="powers_race")],
        [InlineKeyboardButton("🏠 Poderes de Origem", callback_data="powers_origin")],
        [InlineKeyboardButton("👹 Poderes da Tormenta", callback_data="powers_tormenta")],
        [InlineKeyboardButton("↩️ Voltar", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

def create_spell_results_keyboard(spells: List[str]) -> InlineKeyboardMarkup:
    """Create a keyboard with spell results."""
    keyboard = []
    for spell in spells:
        keyboard.append([InlineKeyboardButton(spell, callback_data=f"spell_{spell}")])
    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="magias_menu")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def create_rule_results_keyboard(rules: List[Dict[str, Any]]) -> InlineKeyboardMarkup:
    """Create a keyboard with rule results."""
    keyboard = []
    for rule in rules:
        keyboard.append([InlineKeyboardButton(rule.name, callback_data=f"rule_{rule.name}")])
    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="regras_menu")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def create_power_results_keyboard(powers: List[Dict[str, Any]], power_type: str) -> InlineKeyboardMarkup:
    """Create a keyboard with power results."""
    keyboard = []
    for power in powers:
        keyboard.append([InlineKeyboardButton(power.name, callback_data=f"power_{power_type}_{power.name}")])
    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="powers_menu")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def create_power_results_class_keyboard(powers: List[Dict[str, Any]], power_type: str) -> InlineKeyboardMarkup:
    """Create a keyboard with power results."""
    keyboard = []
    for power in powers:
        keyboard.append([InlineKeyboardButton(power.name, callback_data=f"power_{power_type}_{power.name}")])
    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="powers_class_list")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def create_power_results_race_keyboard(powers: List[Dict[str, Any]], power_type: str) -> InlineKeyboardMarkup:
    """Create a keyboard with power results."""
    keyboard = []
    for power in powers:
        keyboard.append([InlineKeyboardButton(power.name, callback_data=f"power_{power_type}_{power.name}")])
    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="powers_race_list")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def create_spells_by_level_keyboard(spells_by_level: Dict[int, List[str]]) -> InlineKeyboardMarkup:
    """Create a keyboard with spell levels."""
    keyboard = []
    # Only show levels 1-5
    for level in range(1, 6):
        if level in spells_by_level:
            keyboard.append([InlineKeyboardButton(f"Nível {level}", callback_data=f"level_{level}")])

    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="magias_menu")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def create_spells_for_level_keyboard(spells: List[str], level: int) -> InlineKeyboardMarkup:
    """Create a keyboard with spells of a specific level."""
    keyboard = []
    keyboard.append([InlineKeyboardButton(f"Magias de Nível {level}", callback_data="header")])

    for spell_name in sorted(spells):
        keyboard.append([InlineKeyboardButton(spell_name, callback_data=f"spell_{spell_name}")])

    keyboard.append([InlineKeyboardButton("↩️ Voltar para Níveis", callback_data="list_spells")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def create_rules_keyboard(rules: List[Dict[str, Any]]) -> InlineKeyboardMarkup:
    """Create a keyboard with all rules."""
    keyboard = []
    for rule in sorted(rules, key=lambda x: x.name):
        keyboard.append([InlineKeyboardButton(rule.name, callback_data=f"rule_{rule.name}")])

    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="regras_menu")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def create_powers_list_keyboard() -> InlineKeyboardMarkup:
    """Create a keyboard for selecting power types to list."""
    keyboard = [
        [InlineKeyboardButton("🏹 Listar Poderes de Classe", callback_data="list_powers_class")],
        [InlineKeyboardButton("🐺 Listar Poderes de Raça", callback_data="list_powers_race")],
        [InlineKeyboardButton("🏠 Listar Poderes de Origem", callback_data="list_powers_origin")],
        [InlineKeyboardButton("👹 Listar Poderes da Tormenta", callback_data="list_powers_tormenta")],
        [InlineKeyboardButton("💪 Listar Poderes de Combate", callback_data="list_powers_combate")],
        [InlineKeyboardButton("🔮 Listar Poderes de Destino", callback_data="list_powers_destino")],
        [InlineKeyboardButton("🧙 Listar Poderes de Magia", callback_data="list_powers_magia")],
        [InlineKeyboardButton("🛐 Listar Poderes Concedidos", callback_data="list_powers_concedidas")],
        [InlineKeyboardButton("👥 Listar Poderes de Grupo", callback_data="list_powers_grupo")],
        [InlineKeyboardButton("↩️ Voltar", callback_data="poderes_menu")],
        [InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

def create_powers_by_type_keyboard(powers: List[Dict[str, Any]], power_type: str) -> InlineKeyboardMarkup:
    """Create a keyboard with all powers of a specific type."""
    keyboard = []
    for power in sorted(powers, key=lambda x: x.name):
        keyboard.append([InlineKeyboardButton(power.name, callback_data=f"power_{power_type}_{power.name}")])

    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="poderes_menu")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def create_spell_types_keyboard() -> InlineKeyboardMarkup:
    """Create a keyboard with spell types."""
    keyboard = [
        [InlineKeyboardButton("🔮 Arcana", callback_data="spell_type_Arcana")],
        [InlineKeyboardButton("🛐 Divina", callback_data="spell_type_Divina")],
        [InlineKeyboardButton("🌍 Universal", callback_data="spell_type_Universal")],
        [InlineKeyboardButton("↩️ Voltar", callback_data="magias_menu")],
        [InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

def create_spells_by_type_keyboard(spells: List[Spell], spell_type: str) -> InlineKeyboardMarkup:
    """Create a keyboard with spells of a specific type."""
    keyboard = []
    keyboard.append([InlineKeyboardButton(f"Magias do tipo {spell_type}", callback_data="header")])

    for spell in sorted(spells, key=lambda x: x.name):
        keyboard.append([InlineKeyboardButton(f"{spell.name} (Nv {spell.level})", callback_data=f"spell_{spell.name}")])

    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="list_spells_by_type")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def create_search_again_keyboard(search_state: str) -> InlineKeyboardMarkup:
    """Create a keyboard with options to search again or return to main menu."""
    keyboard = [
        [InlineKeyboardButton("🔍 Pesquisar novamente", callback_data=f"search_again_{search_state}")],
        [InlineKeyboardButton("📋 Voltar ao menu principal", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

def create_race_list_keyboard() -> InlineKeyboardMarkup:
    """Create a keyboard with a list of races from Tormenta 20."""
    races = [
        "Humano", "Anão", "Dahllan", "Elfo", "Goblin", "Lefou", 
        "Minotauro", "Qareen", "Golem", "Hynne", "Kliren", "Medusa",
        "Osteon", "Sereia", "Sílfide", "Suraggel", "Trog"
    ]

    keyboard = []
    for race in races:
        keyboard.append([InlineKeyboardButton(race, callback_data=f"powers_race_{race}")])

    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="poderes_menu")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])

    return InlineKeyboardMarkup(keyboard)

def create_class_list_keyboard() -> InlineKeyboardMarkup:
    """Create a keyboard with a list of classes from Tormenta 20."""
    classes = [
        "Arcanista", "Bárbaro", "Bardo", "Bucaneiro", "Caçador", 
        "Cavaleiro", "Clérigo", "Druida", "Guerreiro", "Inventor",
        "Ladino", "Lutador", "Nobre", "Paladino"
    ]

    keyboard = []
    for class_name in classes:
        keyboard.append([InlineKeyboardButton(class_name, callback_data=f"powers_class_{class_name}")])

    keyboard.append([InlineKeyboardButton("↩️ Voltar", callback_data="poderes_menu")])
    keyboard.append([InlineKeyboardButton("📋 Voltar ao Menu Principal", callback_data="back_to_main")])

    return InlineKeyboardMarkup(keyboard)
