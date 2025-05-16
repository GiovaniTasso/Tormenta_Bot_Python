import os

from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from config.settings import BOT_TOKEN, SPELLS_FILE, RULES_FILE, CLASS_POWERS_FILE, RACE_POWERS_FILE, ORIGIN_POWERS_FILE, TORMENTA_POWERS_FILE, COMBAT_POWERS_FILE, DESTINY_POWERS_FILE, MAGIC_POWERS_FILE, GRANTED_POWERS_FILE, GROUP_POWERS_FILE
from src.data.data_loader import load_json_data
from src.data.repositories import SpellRepository, RuleRepository, PowerRepository
from src.domain.services import SpellService, RuleService, PowerService
from src.bot.handlers import CommandHandlers, CallbackHandlers, MessageHandlers
from src.utils.logging_config import setup_logging

# Setup logging
logger = setup_logging()

# Create data directories if they don't exist
os.makedirs(os.path.dirname(SPELLS_FILE), exist_ok=True)
os.makedirs(os.path.dirname(RULES_FILE), exist_ok=True)
os.makedirs(os.path.dirname(CLASS_POWERS_FILE), exist_ok=True)

def main() -> None:
    """Start the bot."""
    # Load data
    spells_data = load_json_data(SPELLS_FILE)
    rules_data = load_json_data(RULES_FILE)
    class_powers_data = load_json_data(CLASS_POWERS_FILE)
    race_powers_data = load_json_data(RACE_POWERS_FILE)
    origin_powers_data = load_json_data(ORIGIN_POWERS_FILE)
    tormenta_powers_data = load_json_data(TORMENTA_POWERS_FILE)
    combat_powers_data = load_json_data(COMBAT_POWERS_FILE)
    destiny_powers_data = load_json_data(DESTINY_POWERS_FILE)
    magic_powers_data = load_json_data(MAGIC_POWERS_FILE)
    granted_powers_data = load_json_data(GRANTED_POWERS_FILE)
    group_powers_data = load_json_data(GROUP_POWERS_FILE)

    # Initialize repositories
    spell_repo = SpellRepository(spells_data)
    rule_repo = RuleRepository(rules_data)
    power_repo = PowerRepository(
        class_powers_data, 
        race_powers_data, 
        origin_powers_data, 
        tormenta_powers_data,
        combat_powers_data,
        destiny_powers_data,
        magic_powers_data,
        granted_powers_data,
        group_powers_data
    )

    # Initialize services
    spell_service = SpellService(spell_repo)
    rule_service = RuleService(rule_repo)
    power_service = PowerService(power_repo)

    # Initialize handlers
    command_handlers = CommandHandlers(spell_service, rule_service, power_service)
    callback_handlers = CallbackHandlers(spell_service, rule_service, power_service)
    message_handlers = MessageHandlers(spell_service, rule_service, power_service)

    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", command_handlers.start))
    application.add_handler(CommandHandler("help", command_handlers.help_command))
    application.add_handler(CallbackQueryHandler(callback_handlers.handle_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handlers.handle_message))

    # Run the bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
