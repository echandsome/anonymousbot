from functools import wraps
from anonymousbot import config


def sep(num, none_is_zero=False):
    if num is None:
        return 0 if none_is_zero is True else None
    return "{:,}".format(num)



async def invalid_command(update, context):
    text = "This command is invalid"
    await update.message.reply_text(text=text, quote=True)


def only_admin(func):
    @wraps(func)
    async def wrapped(update, context, *args, **kwargs):
        if update.message.from_user.id not in config.ADMINS:
            await invalid_command(update, context, *args, **kwargs)
            return
        return await func(update, context, *args, **kwargs)
    return wrapped
    