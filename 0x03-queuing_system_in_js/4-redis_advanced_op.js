import redis from 'redis';
import { promisify } from 'util';


const client = redis.createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

console.log('Redis client connected to the server');

client.hset('HolbertonSchools', 'Portland', '50', redis.print);
client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
client.hset('HolbertonSchools', 'New York', '20', redis.print);
client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
client.hset('HolbertonSchools', 'Cali', '4', redis.print);
client.hset('HolbertonSchools', 'Paris', '2', redis.print);


client.hgetall('HolbertonSchools', (err, data) => {
  console.log(data);
});
