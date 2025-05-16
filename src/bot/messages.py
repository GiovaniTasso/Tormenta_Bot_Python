from ..domain.models import Spell, Rule, Power

def format_spell_details(spell: Spell) -> str:
    """Format spell details for display."""
    # Start with basic spell information
    formatted_text = (
        f"*{spell.name}*\n"
        f"*Nível:* {spell.level}\n"
        f"*Escola:* {spell.school}\n"
        f"*Tempo de Conjuração:* {spell.casting_time}\n"
        f"*Alcance:* {spell.range}\n"
        f"*Alvo:* {spell.target}\n"
        f"*Duração:* {spell.duration}\n"
        f"*Resistência:* {spell.resistance}\n\n"
        f"*Descrição:* {spell.description}"
    )

    # Add enhancements if they exist
    if spell.enhancements and len(spell.enhancements) > 0:
        formatted_text += "\n\n*Aprimoramentos:*"
        for enhancement in spell.enhancements:
            formatted_text += f"\n• *{enhancement.cost}:* {enhancement.description}"

    return formatted_text

def format_rule_details(rule: Rule) -> str:
    """Format rule details for display."""
    return (
        f"*{rule.name}*\n"
        f"*Categoria:* {rule.category}\n\n"
        f"*Descrição:* {rule.description}"
    )

def format_power_details(power: Power) -> str:
    """Format power details for display based on power type."""
    if power.power_type == "class":
        return (
            f"*{power.name}*\n"
            f"*Classe:* {power.class_name}\n"
            f"*Requisitos:* {power.requirements}\n\n"
            f"*Descrição:* {power.description}"
        )
    elif power.power_type == "race":
        return (
            f"*{power.name}*\n"
            f"*Raça:* {power.race}\n"
            f"*Requisitos:* {power.requirements}\n\n"
            f"*Descrição:* {power.description}"
        )
    elif power.power_type == "origin":
        return (
            f"*{power.name}*\n"
            f"*Origem:* {power.origin}\n"
            f"*Requisitos:* {power.requirements}\n\n"
            f"*Descrição:* {power.description}"
        )
    else:  # tormenta
        return (
            f"*{power.name}*\n"
            f"*Requisitos:* {power.requirements}\n\n"
            f"*Descrição:* {power.description}"
        )
