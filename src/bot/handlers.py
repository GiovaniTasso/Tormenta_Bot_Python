from telegram import Update, Message, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from .keyboards import (
    create_main_menu_keyboard,
    create_magias_menu_keyboard,
    create_regras_menu_keyboard,
    create_poderes_menu_keyboard,
    create_list_magias_options_keyboard,
    create_spell_results_keyboard,
    create_rule_results_keyboard,

    create_spells_by_level_keyboard,
    create_spells_for_level_keyboard,
    create_rules_keyboard,
    create_powers_list_keyboard,
    create_powers_by_type_keyboard,
    create_search_again_keyboard,
    create_spell_types_keyboard,
    create_spells_by_type_keyboard,
    create_race_list_keyboard,
    create_class_list_keyboard, create_power_results_class_keyboard, create_power_results_race_keyboard,
    create_power_results_keyboard
)
from .messages import format_spell_details, format_rule_details, format_power_details
from ..domain.services import SpellService, RuleService, PowerService


class CommandHandlers:
    def __init__(self, spell_service: SpellService, rule_service: RuleService, power_service: PowerService):
        self.spell_service = spell_service
        self.rule_service = rule_service
        self.power_service = power_service

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        keyboard = create_main_menu_keyboard()
        await update.message.reply_text(
            "😊 Bem-vindo ao Bot de Tormenta 20! Escolha uma opção: 😊",
            reply_markup=keyboard,
        )

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""
        await update.message.reply_text(
            "Este bot permite consultar informações sobre Tormenta 20.\n\n"
            "Comandos disponíveis:\n"
            "/start - Mostrar menu principal\n"
            "/help - Mostrar esta mensagem de ajuda\n"
        )

class CallbackHandlers:
    def __init__(self, spell_service: SpellService, rule_service: RuleService, power_service: PowerService):
        self.spell_service = spell_service
        self.rule_service = rule_service
        self.power_service = power_service

    async def handle_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle button presses."""
        query = update.callback_query
        await query.answer()

        # Main menu options
        if query.data == "magias_menu":
            keyboard = create_magias_menu_keyboard()
            await query.message.edit_text(
                " 🧙‍♂️ Menu de Magias:🧙‍♂️ ",
                reply_markup=keyboard,
            )

        elif query.data == "regras_menu":
            keyboard = create_regras_menu_keyboard()
            await query.message.edit_text(
                "📖 Menu de Regras: 📖",
                reply_markup=keyboard,
            )

        elif query.data == "poderes_menu":
            keyboard = create_poderes_menu_keyboard()
            await query.message.edit_text(
                "⚡ Menu de Poderes: ⚡",
                reply_markup=keyboard,
            )

        # Magias submenu options
        elif query.data == "search_spells":
            await query.message.reply_text(
                "✨ Digite o nome da magia que deseja buscar: ✨"
            )
            context.user_data["state"] = "searching_spells"

        elif query.data == "list_magias_options":
            keyboard = create_list_magias_options_keyboard()
            await query.message.reply_text(
                "🎇 Como deseja listar as magias?",
                reply_markup=keyboard,
            )

        elif query.data == "list_spells":
            await self.list_all_spells(query.message, context)

        elif query.data == "list_spells_by_type":
            keyboard = create_spell_types_keyboard()
            await query.message.reply_text(
                "✨ Escolha o tipo de magia:✨",
                reply_markup=keyboard,
            )

        elif query.data.startswith("spell_type_"):
            spell_type = query.data[11:]  # Remove "spell_type_" prefix
            await self.list_spells_by_type(query.message, context, spell_type)

        elif query.data.startswith("level_"):
            level = int(query.data[6:])  # Remove "level_" prefix
            await self.list_spells_for_level(query.message, context, level)

        # Regras submenu options
        elif query.data == "list_rules":
            await self.list_all_rules(query.message, context)

        elif query.data == "rules":
            await query.message.reply_text(
                "🔍 Digite o termo de regra que deseja buscar:"
            )
            context.user_data["state"] = "searching_rules"

        # Poderes submenu options
        elif query.data == "list_powers":
            keyboard = create_powers_list_keyboard()
            await query.message.reply_text(
                "📖 Escolha o tipo de poderes para listar:",
                reply_markup=keyboard,
            )

        elif query.data.startswith("list_powers_"):
            power_type = query.data.split("_")[2]
            await self.list_powers_by_type(query.message, context, power_type)

        elif query.data == "powers_race_list":
            keyboard = create_race_list_keyboard()
            await query.message.edit_text(
                "🧌 Escolha uma raça:🧌",
                reply_markup=keyboard,
            )

        elif query.data == "powers_class_list":
            keyboard = create_class_list_keyboard()
            await query.message.edit_text(
                "🧙 Escolha uma classe:🏹",
                reply_markup=keyboard,
            )

        elif query.data.startswith("powers_"):
            parts = query.data.split("_")
            power_type = parts[1]

            # Handle race and class specific selections
            if power_type == "race" and len(parts) > 2:
                race_name = parts[2]
                await query.message.edit_text(
                    f"Poderes da raça {race_name}:",
                    reply_markup=create_power_results_race_keyboard(
                        self.power_service.get_powers_by_race(race_name), "race"
                    ),
                )
            elif power_type == "class" and len(parts) > 2:
                class_name = parts[2]
                await query.message.edit_text(
                    f"Poderes da classe {class_name}:",
                    reply_markup=create_power_results_class_keyboard(
                        self.power_service.get_powers_by_class(class_name), "class"
                    ),
                )
            else:
                # Handle other power types
                await self.list_powers_by_type(query.message, context, power_type)

        elif query.data.startswith("search_again_"):
            search_state = query.data[12:]  # Remove "search_again_" prefix
            context.user_data["state"] = search_state

            if search_state == "searching_spells":
                await query.message.reply_text("✨ Digite o nome da magia que deseja buscar:")
            elif search_state == "searching_rules":
                await query.message.reply_text("📖 Digite o termo de regra que deseja buscar:")
            elif search_state.startswith("searching_powers_"):
                power_type = search_state.split("_")[2]
                type_name = {
                    "class": "classe",
                    "race": "raça",
                    "origin": "origem",
                    "tormenta": "tormenta",
                    "combate": "combate",
                    "destino": "destino",
                    "magia": "magia",
                    "concedidas": "concedidas",
                    "grupo": "grupo"
                }.get(power_type, power_type)
                await query.message.reply_text(f"Digite o nome do poder de {type_name} que deseja buscar:")

        elif query.data == "back_to_main":
            keyboard = create_main_menu_keyboard()
            await query.message.edit_text(
                "🎲 Bem-vindo ao Bot de Tormenta 20! Escolha uma opção:🎲",
                reply_markup=keyboard,
            )

        elif query.data.startswith("spell_"):
            spell_name = query.data[6:]  # Remove "spell_" prefix
            await self.show_spell_details(query.message, spell_name)

        elif query.data.startswith("rule_"):
            rule_name = query.data[5:]  # Remove "rule_" prefix
            await self.show_rule_details(query.message, rule_name)

        elif query.data.startswith("power_"):
            # Format: power_type_name
            parts = query.data.split("_", 2)
            if len(parts) == 3:
                power_type = parts[1]
                power_name = parts[2]
                await self.show_power_details(query.message, power_type, power_name)

    async def list_all_spells(self, message: Message, context: ContextTypes.DEFAULT_TYPE) -> None:
        """List all spells with their names and levels."""
        spells = self.spell_service.get_all_spells()

        if not spells:
            await message.reply_text("Desculpe, não foi possível carregar a lista de magias.")
            return

        # Group spells by level
        spells_by_level = {}
        for spell in spells:
            level = spell.level
            if level not in spells_by_level:
                spells_by_level[level] = []
            spells_by_level[level].append(spell.name)

        keyboard = create_spells_by_level_keyboard(spells_by_level)

        await message.reply_text(
            "Lista de Magias por Nível:",
            reply_markup=keyboard,
        )

    async def list_spells_by_type(self, message: Message, context: ContextTypes.DEFAULT_TYPE, spell_type: str) -> None:
        """List all spells of a specific type."""
        spells = self.spell_service.get_spells_by_type(spell_type)

        if not spells:
            await message.reply_text(f"Desculpe, não foi possível encontrar magias do tipo {spell_type}.")
            return

        keyboard = create_spells_by_type_keyboard(spells, spell_type)

        await message.reply_text(
            f"Lista de Magias do tipo {spell_type}:",
            reply_markup=keyboard,
        )

    async def list_spells_for_level(self, message: Message, context: ContextTypes.DEFAULT_TYPE, level: int) -> None:
        """List all spells of a specific level."""
        spells = self.spell_service.get_spells_by_level(level)

        if not spells:
            await message.reply_text(f"Desculpe, não foi possível encontrar magias de nível {level}.")
            return

        spell_names = [spell.name for spell in spells]
        keyboard = create_spells_for_level_keyboard(spell_names, level)

        await message.reply_text(
            f"Lista de Magias de Nível {level}:",
            reply_markup=keyboard,
        )

    async def list_all_rules(self, message: Message, context: ContextTypes.DEFAULT_TYPE) -> None:
        """List all rules."""
        rules = self.rule_service.get_all_rules()

        if not rules:
            await message.reply_text("Desculpe, não foi possível carregar a lista de regras.")
            return

        keyboard = create_rules_keyboard(rules)

        await message.reply_text(
            "Lista de Regras:",
            reply_markup=keyboard,
        )

    async def list_powers_by_type(self, message: Message, context: ContextTypes.DEFAULT_TYPE, power_type: str) -> None:
        """List all powers of a specific type."""
        powers = self.power_service.get_all_powers_by_type(power_type)

        if not powers:
            type_name = {
                "class": "classe",
                "race": "raça",
                "origin": "origem",
                "tormenta": "tormenta",
                "combate": "combate",
                "destino": "destino",
                "magia": "magia",
                "concedidas": "concedidas",
                "grupo": "grupo"
            }.get(power_type, power_type)
            await message.reply_text(f"Desculpe, não foi possível carregar a lista de poderes de {type_name}.")
            return

        keyboard = create_powers_by_type_keyboard(powers, power_type)

        type_name = {
            "class": "Classe",
            "race": "Raça",
            "origin": "Origem",
            "tormenta": "Tormenta",
            "combate": "Combate",
            "destino": "Destino",
            "magia": "Magia",
            "concedidas": "Concedidas",
            "grupo": "Grupo"
        }.get(power_type, power_type.capitalize())

        await message.reply_text(
            f"Lista de Poderes de {type_name}:",
            reply_markup=keyboard,
        )

    async def show_spell_details(self, message: Message, spell_name: str) -> None:
        """Show details for a specific spell."""
        spell = self.spell_service.get_spell_details(spell_name)

        if spell:
            formatted_message = format_spell_details(spell)
            keyboard = [
                [InlineKeyboardButton("🔙 Voltar", callback_data="magias_menu")],
                [InlineKeyboardButton("🔙 Voltar ao Menu Principal", callback_data="back_to_main")]
            ]
            await message.reply_text(formatted_message, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
        else:
            await message.reply_text(f"Desculpe, não encontrei detalhes para a magia '{spell_name}'.")

    async def show_rule_details(self, message: Message, rule_name: str) -> None:
        """Show details for a specific rule."""
        rule = self.rule_service.get_rule_details(rule_name)

        if rule:
            formatted_message = format_rule_details(rule)
            keyboard = [
                [InlineKeyboardButton("🔙 Voltar", callback_data="regras_menu")],
                [InlineKeyboardButton("🔙 Voltar ao Menu Principal", callback_data="back_to_main")]
            ]
            await message.reply_text(formatted_message, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
        else:
            await message.reply_text(f"Desculpe, não encontrei detalhes para a regra '{rule_name}'.")

    async def show_power_details(self, message: Message, power_type: str, power_name: str) -> None:
        """Show details for a specific power."""
        power = self.power_service.get_power_details(power_type, power_name)

        if power:
            formatted_message = format_power_details(power)
            keyboard = [
                [InlineKeyboardButton("🔙 Voltar", callback_data="poderes_menu")],
                [InlineKeyboardButton("🔙 Voltar ao Menu Principal", callback_data="back_to_main")]
            ]
            await message.reply_text(formatted_message, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
        else:
            type_name = {
                "class": "classe",
                "race": "raça",
                "origin": "origem",
                "tormenta": "tormenta",
                "combate": "combate",
                "destino": "destino",
                "magia": "magia",
                "concedidas": "concedidas",
                "grupo": "grupo"
            }.get(power_type, power_type)
            await message.reply_text(f"Desculpe, não encontrei detalhes para o poder de {type_name} '{power_name}'.")

class MessageHandlers:
    def __init__(self, spell_service: SpellService, rule_service: RuleService, power_service: PowerService):
        self.spell_service = spell_service
        self.rule_service = rule_service
        self.power_service = power_service

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle user messages based on the current state."""
        if "state" not in context.user_data:
            command_handlers = CommandHandlers(self.spell_service, self.rule_service, self.power_service)
            await command_handlers.start(update, context)
            return

        state = context.user_data["state"]
        text = update.message.text.lower()

        if state == "searching_spells":
            matching_spells = self.spell_service.search_spells(text)

            if matching_spells:
                keyboard = create_spell_results_keyboard([spell.name for spell in matching_spells])

                await update.message.reply_text(
                    f"Resultados para '{text}':",
                    reply_markup=keyboard,
                )
            else:
                keyboard = create_search_again_keyboard("searching_spells")
                await update.message.reply_text(
                    f"Nenhuma magia encontrada para '{text}'.",
                    reply_markup=keyboard
                )
                return  # Don't reset state yet

        elif state == "searching_rules":
            matching_rules = self.rule_service.search_rules(text)

            if matching_rules:
                keyboard = create_rule_results_keyboard(matching_rules)

                await update.message.reply_text(
                    f"Resultados para '{text}':",
                    reply_markup=keyboard,
                )
            else:
                keyboard = create_search_again_keyboard("searching_rules")
                await update.message.reply_text(
                    f"Nenhuma regra encontrada para '{text}'.",
                    reply_markup=keyboard
                )
                return  # Don't reset state yet

        elif state.startswith("searching_powers_"):
            power_type = state.split("_")[2]
            matching_powers = self.power_service.search_powers(power_type, text)

            if matching_powers:
                keyboard = create_power_results_keyboard(matching_powers, power_type)

                await update.message.reply_text(
                    f"Resultados para '{text}':",
                    reply_markup=keyboard,
                )
            else:
                type_name = {
                    "class": "classe",
                    "race": "raça",
                    "origin": "origem",
                    "tormenta": "tormenta",
                    "combate": "combate",
                    "destino": "destino",
                    "magia": "magia",
                    "concedidas": "concedidas",
                    "grupo": "grupo"
                }.get(power_type, power_type)
                keyboard = create_search_again_keyboard(state)
                await update.message.reply_text(
                    f"Nenhum poder de {type_name} encontrado para '{text}'.",
                    reply_markup=keyboard
                )
                return  # Don't reset state yet

        # Reset state only if we found results
        context.user_data["state"] = None
