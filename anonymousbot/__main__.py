import logging

# files
from anonymousbot import config
from anonymousbot import commands
from anonymousbot import messages
from anonymousbot import utils
from anonymousbot import albums
from anonymousbot import custom_filters
from anonymousbot import constants
from anonymousbot import dbwrapper

from telegram import Bot
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Application
)

from telegram.ext import filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# disable apscheduler logging
aps_logger = logging.getLogger('apscheduler')
aps_logger.setLevel(logging.WARNING)


# disable httpx logging
httpx_logger = logging.getLogger('httpx')
httpx_logger.setLevel(logging.WARNING)


async def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


async def before_serving(application):
    constants.GET_ME = await application.bot.getMe()
    await dbwrapper.create_db()


def main():
    print("\nrunning...")
    # define the application
    application = Application.builder().token(config.BOT_TOKEN).post_init(before_serving).build()
    # messages
    application.add_handler(MessageHandler(filters.ALL, messages.before_processing), 0)
    # albums
    application.add_handler(MessageHandler(custom_filters.album, albums.collect_album_items), 1)
    # messages
    application.add_handler(MessageHandler(filters.ALL, messages.process_message, block=False), 1)
    # commands
    application.add_handler(CommandHandler('stats', commands.stats), 2)
    application.add_handler(CommandHandler(('start', 'help'), commands.help_command, block=False), 2)
    application.add_handler(CommandHandler('disablewebpagepreview', commands.disable_web_page_preview, block=False), 2)
    application.add_handler(CommandHandler('removecaption', commands.remove_caption, block=False), 2)
    application.add_handler(CommandHandler('removebuttons', commands.remove_buttons, block=False), 2)
    application.add_handler(CommandHandler('addcaption', commands.add_caption, block=False), 2)
    application.add_handler(CommandHandler('addbuttons', commands.add_buttons, block=False), 2)
    application.add_handler(CommandHandler('removespoiler', commands.remove_spoiler, block=False), 2)
    application.add_handler(CommandHandler('addspoiler', commands.add_spoiler, block=False), 2)
    application.add_handler(MessageHandler(filters.COMMAND, utils.invalid_command, block=False), 2)


    # handle errors
    application.add_error_handler(error)

    application.run_polling()


if __name__ == '__main__':
    main()
