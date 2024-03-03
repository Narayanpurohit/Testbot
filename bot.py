const { Telegraf } = require('telegraf');

const bot = new Telegraf('6991774790:AAFsYGdXqc7gvxruvklWESj9KPUG3DGOBjA');

// Command handler for /start
bot.start((ctx) => {
  ctx.reply('Hello! This is your Telegram bot.');
});

// Command handler for /echo
bot.command('echo', (ctx) => {
  const message = ctx.message.text.split(' ').slice(1).join(' ');
  ctx.reply(`You said: ${message}`);
});

// Handle text messages
bot.on('text', (ctx) => {
  ctx.reply('I received a text message.');
});

// Start the bot
bot.launch().then(() => {
  console.log('Bot started');
});
