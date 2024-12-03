import { Item } from '../models/Item'

var baseUrl = "http://127.0.0.1:5555/items";

export const getItems = async (): Promise<Item[]> => {
    return (await fetch(baseUrl)).json();
};

