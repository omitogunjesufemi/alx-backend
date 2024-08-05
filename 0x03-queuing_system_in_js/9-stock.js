import express, { response } from "express";
import redis from 'redis';
import { promisify } from "util";

const app = express();
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (err) =>{
    console.log('Redis client not connected to the server: ', err);
});

console.log('Redis client connected to the server');

const listProducts = [
    {itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4},
    {itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10},
    {itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2},
    {itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5}
];

function getItemById (id) {
    for (const product of listProducts) {
        if (product.itemId == id) {
            return product;
        }
    }
    return null;
}

function reserveStockById (itemId, stock) {
    return client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById (itemId) {
    const stock = await getAsync(`item.${itemId}`);
    if (stock !== null) {
        return stock;
    }
    return null;
}

app.get('/list_products', (request, response) => {
    response.json(listProducts);
});

app.get('/list_products/:itemId', async (request, response) => {
    const itemId = request.params.itemId;
    const product = getItemById(itemId);
    const stock = await getCurrentReservedStockById(itemId);

    if (product == null) {
        response.json({ status: 'Product not found' });
        return;
    }

    const currentQuantity = product.initialAvailableQuantity - (stock || 0);

    response.json({
        itemId: product.itemId,
        itemName: product.itemName,
        price: product.price,
        initialAvailableQuantity: product.initialAvailableQuantity,
        currentQuantity: currentQuantity
    });
});

app.get('/reserve_product/:itemId', (request, response) => {
    const itemId = request.params.itemId;
    const product = getItemById(itemId);

    if (product == null) {
        response.json({ status: 'Product not found' });
        return;
    }

    if (product.initialAvailableQuantity < 0) {
        response.json({status: 'Not enough stock available', itemId: itemId});
        return;
    }

    reserveStockById(itemId, 1);
    response.json({status: 'Reservation confirmed', itemId: itemId})
});

app.listen(1245);
