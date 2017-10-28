# ForwardsCoverBot - don't let people on telegram forward with your name on the forward label
# Copyright (C) 2017  Dario <dariomsn@hotmail.it> (github.com/91DarioDev)

# ForwardsCoverBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# ForwardsCoverBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with ForwardsCoverBot.  If not, see <http://www.gnu.org/licenses/>.

from config import configfile

from telegram import Bot

GET_ME = Bot(configfile.BOT_TOKEN).getMe()
