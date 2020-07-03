import discord
import logging
import asyncio
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from redbot.core import commands
from datetime import datetime, timedelta

class AuditLogger(commands.Cog):
    """Custom Cog Made By Serum#2004 this was made for servers in need of in depth audit logs"""
    
    @checks.admin_or_permissions(manage_guild)
    @commands.guild_only()
    @commands.command()
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

class LogHandle:
    """basic wrapper for logfile handles, used to keep track of stale handles"""
    def __init__(self, path, time=None, mode='a', buf=1):
        self.handle = open(path, mode, buf, errors='backslashreplace')
        self.lock = asyncio.Lock()

        if time:
            self.time = time
        else:
            self.time = datetime.fromtimestamp(os.path.getmtime(path))

    async def write(self, value):
        async with self.lock:
            self._write(value)

    def close(self):
        self.handle.close()

    def _write(self, value):
        self.time = datetime.utcnow()
        self.handle.write(value)
