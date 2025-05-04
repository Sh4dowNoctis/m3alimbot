# components/buttons.py
import discord
from discord.ext import commands
from discord.ui import View, Button

class ConfirmPurgeView(View):
    def __init__(self, ctx: commands.context.Context, messages_to_delete):
        super().__init__(timeout=15)
        self.ctx = ctx
        self.messages = messages_to_delete
        self.value = None


    @discord.ui.button(label="✅ Confirm", style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: Button):
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("Only the command author can confirm this.", ephemeral=True)
            return
        await interaction.response.edit_message(content=f"🧹 Deleting {len(self.messages)-1} messages...", view=None, delete_after=3)
        await self.ctx.channel.delete_messages(self.messages)
        self.value = True
        self.stop()
        
        
    @discord.ui.button(label="❌ Cancel", style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(content="🚫 Purge cancelled.", view=None, delete_after=3)
        self.value = False
        self.stop()
