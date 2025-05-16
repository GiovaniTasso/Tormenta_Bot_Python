from typing import List, Dict, Any, Optional
from ..domain.models import Spell, SpellEnhancement, Rule, Power

class SpellRepository:
    def __init__(self, data: Dict[str, Any]):
        # Convert Portuguese field names to English for compatibility with Spell class
        spells_data = []
        for spell in data.get('magias', []):
            if spell:
                # Process enhancements if they exist
                enhancements = []
                if 'aprimoramentos' in spell and spell['aprimoramentos']:
                    for enhancement in spell['aprimoramentos']:
                        enhancements.append(SpellEnhancement(
                            cost=enhancement.get('custo', ''),
                            description=enhancement.get('descrição', '')
                        ))

                spells_data.append({
                    'name': spell.get('nome', ''),
                    'level': spell.get('nivel', 0),
                    'school': spell.get('escola', ''),
                    'type': spell.get('tipo', ''),
                    'casting_time': spell.get('tempo_de_conjuracao', '') or spell.get('execução', ''),
                    'range': spell.get('alcance', ''),
                    'target': spell.get('alvo', ''),
                    'duration': spell.get('duracao', '') or spell.get('duração', ''),
                    'resistance': spell.get('resistencia', ''),
                    'description': spell.get('descricao', '') or spell.get('descrição', ''),
                    'enhancements': enhancements
                })
        self.spells = [Spell(**spell) for spell in spells_data] if spells_data else []

    def find_by_name(self, name: str) -> List[Spell]:
        """Find spells by name (case-insensitive partial match)."""
        name = name.lower()
        return [spell for spell in self.spells if name in spell.name.lower()]

    def get_by_name(self, name: str) -> Optional[Spell]:
        """Get a spell by its exact name."""
        for spell in self.spells:
            if spell.name == name:
                return spell
        return None

    def get_all(self) -> List[Spell]:
        """Get all spells."""
        return self.spells

    def get_by_type(self, spell_type: str) -> List[Spell]:
        """Get all spells of a specific type."""
        return [spell for spell in self.spells if spell.type.lower() == spell_type.lower()]

    def get_by_level(self, level: int) -> List[Spell]:
        """Get all spells of a specific level."""
        return [spell for spell in self.spells if spell.level == level]

class RuleRepository:
    def __init__(self, data: Dict[str, Any]):
        self.rules = [Rule(**rule) for rule in data.get('rules', [])] if data else []

    def find_by_name_or_description(self, text: str) -> List[Rule]:
        """Find rules by name or description (case-insensitive partial match)."""
        text = text.lower()
        return [rule for rule in self.rules if text in rule.name.lower() or text in rule.description.lower()]

    def get_by_name(self, name: str) -> Optional[Rule]:
        """Get a rule by its exact name."""
        for rule in self.rules:
            if rule.name == name:
                return rule
        return None

    def get_all(self) -> List[Rule]:
        """Get all rules."""
        return self.rules

class PowerRepository:
    def __init__(self, class_data: Dict[str, Any], race_data: Dict[str, Any], 
                 origin_data: Dict[str, Any], tormenta_data: Dict[str, Any],
                 combat_data: Dict[str, Any] = None, destiny_data: Dict[str, Any] = None,
                 magic_data: Dict[str, Any] = None, granted_data: Dict[str, Any] = None,
                 group_data: Dict[str, Any] = None):
        self.powers = []

        # Load class powers
        if class_data and 'powers' in class_data:
            for power in class_data['powers']:
                power_obj = Power(
                    name=power['name'],
                    description=power['description'],
                    requirements=power['requirements'],
                    power_type="class",
                    class_name=power.get('class')
                )
                self.powers.append(power_obj)

        # Load race powers
        if race_data and 'powers' in race_data:
            for power in race_data['powers']:
                power_obj = Power(
                    name=power['name'],
                    description=power['description'],
                    requirements=power['requirements'],
                    power_type="race",
                    race=power.get('race')
                )
                self.powers.append(power_obj)

        # Load origin powers
        if origin_data and 'powers' in origin_data:
            for power in origin_data['powers']:
                power_obj = Power(
                    name=power['name'],
                    description=power['description'],
                    requirements=power['requirements'],
                    power_type="origin",
                    origin=power.get('origin')
                )
                self.powers.append(power_obj)

        # Load tormenta powers
        if tormenta_data and 'powers' in tormenta_data:
            for power in tormenta_data['powers']:
                power_obj = Power(
                    name=power['name'],
                    description=power['description'],
                    requirements=power['requirements'],
                    power_type="tormenta"
                )
                self.powers.append(power_obj)

        # Load combat powers
        if combat_data and 'powers' in combat_data:
            for power in combat_data['powers']:
                power_obj = Power(
                    name=power['name'],
                    description=power['description'],
                    requirements=power['requirements'],
                    power_type="combate"
                )
                self.powers.append(power_obj)

        # Load destiny powers
        if destiny_data and 'powers' in destiny_data:
            for power in destiny_data['powers']:
                power_obj = Power(
                    name=power['name'],
                    description=power['description'],
                    requirements=power['requirements'],
                    power_type="destino"
                )
                self.powers.append(power_obj)

        # Load magic powers
        if magic_data and 'powers' in magic_data:
            for power in magic_data['powers']:
                power_obj = Power(
                    name=power['name'],
                    description=power['description'],
                    requirements=power['requirements'],
                    power_type="magia"
                )
                self.powers.append(power_obj)

        # Load granted powers
        if granted_data and 'powers' in granted_data:
            for power in granted_data['powers']:
                power_obj = Power(
                    name=power['name'],
                    description=power['description'],
                    requirements=power['requirements'],
                    power_type="concedidas"
                )
                self.powers.append(power_obj)

        # Load group powers
        if group_data and 'powers' in group_data:
            for power in group_data['powers']:
                power_obj = Power(
                    name=power['name'],
                    description=power['description'],
                    requirements=power['requirements'],
                    power_type="grupo"
                )
                self.powers.append(power_obj)

    def find_by_type_and_text(self, power_type: str, text: str) -> List[Power]:
        """Find powers by type and name/description (case-insensitive partial match)."""
        text = text.lower()
        return [
            power for power in self.powers 
            if power.power_type == power_type and 
            (text in power.name.lower() or text in power.description.lower())
        ]

    def get_by_type_and_name(self, power_type: str, name: str) -> Optional[Power]:
        """Get a power by its type and exact name."""
        for power in self.powers:
            if power.power_type == power_type and power.name == name:
                return power
        return None

    def get_all_by_type(self, power_type: str) -> List[Power]:
        """Get all powers of a specific type."""
        return [power for power in self.powers if power.power_type == power_type]

    def get_powers_by_class(self, class_name: str) -> List[Power]:
        """Get all powers for a specific class."""
        return [power for power in self.powers if power.power_type == "class" and power.class_name == class_name]

    def get_powers_by_race(self, race_name: str) -> List[Power]:
        """Get all powers for a specific race (including 'Vários' as wildcard)."""
        result = []
        for power in self.powers:
            if power.power_type != "race":
                continue

            # Caso especial para "Vários"
            if power.race.strip().lower() == "várias":
                result.append(power)
                continue

            # Lógica normal para outras raças
            if any(r.strip().startswith(race_name)
                   for r in power.race.split(",")):
                result.append(power)

        return result