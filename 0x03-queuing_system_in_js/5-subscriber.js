import { count } from 'console';
import { channel } from 'diagnostics_channel';
import redis from 'redis';
import { promisify } from 'util';


const client = redis.createClient();
const clChannel = 'holberton school channel';

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

console.log('Redis client connected to the server');

client.on('message', (channel, message) => {
  if (message == 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }

  console.log(message);
});

client.subscribe(clChannel);
