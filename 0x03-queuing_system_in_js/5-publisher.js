import redis from 'redis';

const client = redis.createClient();
const clChannel = 'holberton school channel';

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

console.log('Redis client connected to the server');

function publishMessage(message, time) {

  client.publish(clChannel, message);
  console.log(message);

}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);