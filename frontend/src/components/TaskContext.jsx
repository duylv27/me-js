import React, { createContext, useState, useContext, useEffect, useRef } from "react";

import { getItems } from "@services/ItemService.ts";

const TaskContext = createContext();

export const useTask = () => {
    return useContext(TaskContext);
};

const TaskProvider = ({ children }) => {

    const [tasks, setTasks] = useState([]);
    const hasFetchedData = useRef(false);

    const updateStatus = (id, status) => {
        if (status >= 0 && status <= 4) {
            setTasks(
                (prevList) => prevList.map(item => item.id === id ? {...item, status} : item)
            );
        }
    };

    const addItem = (newItem) => {
        setTasks(
            (prevList) => [...prevList, newItem]
        );
    };

    useEffect(() => {
        // console.log("Updated tasks:", tasks);
    }, [tasks]);

    const deleteItem = (id) => {
        setTasks(
            (prevList) => prevList.filter(item => item.id !== id)
        );
    };

    const updateItem = (id, updatedItem) => {
        setTasks(
            (prevList) => prevList.map(item => item.id === id ? updatedItem : item)
        );
    };

    useEffect(() => {
        if (!hasFetchedData.current) {
            hasFetchedData.current = true;
            getItems()
            .then(data => setTasks(data))
            .catch(e => console.error("Error fetching tasks:", e));
        }
    }, []);

    return (
        <TaskContext.Provider value={{ tasks, deleteItem, addItem, updateItem, updateStatus }}>
            {children}
        </TaskContext.Provider>
    );
};

export default TaskProvider