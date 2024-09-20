import { createClient, print } from 'redis';
import {promisify } from 'util';

const client = createClient()
	.on('connect', () => console.log('Redis client connected to the server'))
	.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));

const async_func = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, print);
}

const displaySchoolValue = async (schoolName) => {
	try {
		const value = await	async_func(schoolName);
		console.log(value);
	} catch (err) {
			console.log(err);
		}
	}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
