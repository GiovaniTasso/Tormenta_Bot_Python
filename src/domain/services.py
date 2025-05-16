from typing import List, Optional
from ..data.repositories import SpellRepository, RuleRepository, PowerRepository
from .models import Spell, Rule, Power

class SpellService:
    def __init__(self, repository: SpellRepository):
        self.repository = repository

    def search_spells(self, query: str) -> List[Spell]:
        """Search for spells by name."""
        return self.repository.find_by_name(query)

    def get_spell_details(self, name: str) -> Optional[Spell]:
        """Get details for a specific spell."""
        return self.repository.get_by_name(name)

    def get_all_spells(self) -> List[Spell]:
        """Get all spells."""
        return self.repository.get_all()

    def get_spells_by_type(self, spell_type: str) -> List[Spell]:
        """Get all spells of a specific type."""
        return self.repository.get_by_type(spell_type)

    def get_spells_by_level(self, level: int) -> List[Spell]:
        """Get all spells of a specific level."""
        return self.repository.get_by_level(level)

class RuleService:
    def __init__(self, repository: RuleRepository):
        self.repository = repository

    def search_rules(self, query: str) -> List[Rule]:
        """Search for rules by name or description."""
        return self.repository.find_by_name_or_description(query)

    def get_rule_details(self, name: str) -> Optional[Rule]:
        """Get details for a specific rule."""
        return self.repository.get_by_name(name)

    def get_all_rules(self) -> List[Rule]:
        """Get all rules."""
        return self.repository.get_all()

class PowerService:
    def __init__(self, repository: PowerRepository):
        self.repository = repository

    def search_powers(self, power_type: str, query: str) -> List[Power]:
        """Search for powers by type and name/description."""
        return self.repository.find_by_type_and_text(power_type, query)

    def get_power_details(self, power_type: str, name: str) -> Optional[Power]:
        """Get details for a specific power."""
        return self.repository.get_by_type_and_name(power_type, name)

    def get_all_powers_by_type(self, power_type: str) -> List[Power]:
        """Get all powers of a specific type."""
        return self.repository.get_all_by_type(power_type)

    def get_powers_by_class(self, class_name: str) -> List[Power]:
        """Get all powers for a specific class."""
        return self.repository.get_powers_by_class(class_name)

    def get_powers_by_race(self, race_name: str) -> List[Power]:
        """Get all powers for a specific race."""
        return self.repository.get_powers_by_race(race_name)
