import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {

  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
	} else {
		console.log(message);
	}
});

