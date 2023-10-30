---
title: Discord Bot
---

A discord bot is very powerful. One can program it to do anything.

1. Go to https://discord.com/developers/applications to create an applicaiton and bot
2. Go to **Bot** tab and enable the privileged Gateway Intents. This is needed for bot to read messages.
    ![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/23/8a410991-0a1c-4b7b-b0c9-ad9d4f863e44.png)
3. Go to **OAuth2** tab and select the **bot** scope. Select required permissions (choose administrator to get all permission). Copy the link and open it in a new tab. Select the server you want to add the bot to and click **Authorize**.
    ![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/23/d0c4e4c3-dc45-465c-b5cf-87b5c0739a25.png)
4. Go to **Bot** tab and copy the **Token**. The token is used to login to the bot.

## Sample Code

### Python

`pip install -U discord.py`

```python
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')
        if message.author.bot:
            return;
        await message.channel.send("I am bot")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('TOKEN_HERE')
```

### JavaScript

`npm i discord.js`

Note that, JavaScript version requires `GuildMessages` and `Guilds` intents to be enabled, while Python version does not.

```js
const { Client, IntentsBitField } = require("discord.js");
const token = "TOKEN_HERE";

// Create a new client instance
const client = new Client({
  intents: [
    IntentsBitField.Flags.MessageContent,
    IntentsBitField.Flags.GuildMessages,
    IntentsBitField.Flags.Guilds,
  ],
});

// When the client is ready, run this code
client.once("ready", () => {
  console.log("Bot is online!");
});

// Listen for messages
client.on("messageCreate", (message) => {
  // Ignore messages from bots
  if (message.author.bot) return;

  // Log the message content to the console
  console.log(`Message received: ${message.content}`);
  message.channel.send("hey I am bot");
});

// Replace 'YOUR_BOT_TOKEN' with your actual bot token
client.login(token);
```

Use bot to clear all messages in a channel



```js
client.on("messageCreate", (message) => {
  // Ignore messages from bots
  if (message.author.bot) return;

  if (message.content === '!clear') {
    message.channel.messages.fetch().then(messages => {
      message.channel.bulkDelete(messages);
    });
  }
});
```

## Reference

- [Discord Bot with Python YouTube Playlist](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAHdJdtEl0-XiRfPRAvpbSz)