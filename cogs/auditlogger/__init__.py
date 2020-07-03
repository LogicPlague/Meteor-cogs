from .auditlogger import AuditLogger

def setup(bot):
    bot.add_cog(AuditLogger())