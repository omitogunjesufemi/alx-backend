import redis from 'redis';
import { promisify } from 'util';

async function main() {
  const client = redis.createClient();

  client.on('error', (err) => {
    console.log('Redis client not connected to the server: ', err);
  });

  console.log('Redis client connected to the server');

  function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print)
  }

  const getAsync = promisify(client.get).bind(client);

  async function displaySchoolValue(schoolName) {
    const value = await getAsync(schoolName);
    console.log(value);
  }

  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

main();
