import React, { useEffect, useState } from "react";
import { useTask } from "@components/TaskContext.jsx";

const Task = ({ item }) => {

    const { tasks, deleteItem, updateItem, updateStatus } = useTask();

    const [id, _] = useState(item.id);
    const [content, setContent] = useState(item.content);
    const [priority, setPriority] = useState(item.priority);

    useEffect(() => {
        console.log("Render Tasks");
    }, []);

    useEffect(() => {
        // Hooks change on content and priority
    }, [content, priority]);

    const removeTask = (id) => {
        deleteItem(id);
        console.log(tasks);
    }

    const showTasks = () =>{
        console.log(tasks);
    }

    // Handle changes for content
    const handleContentChange = (e) => {
        setContent(e.target.value);
        const updatedItem = { ...item, content: e.target.value };
        updateItem(item.id, updatedItem);
    };

    // Handle changes for priority
    const handlePriorityChange = (e) => {
        setPriority(e.target.value);
        const updatedItem = { ...item, priority: e.target.value };
        updateItem(item.id, updatedItem);
    };

    return (
        <div className="card">
            <div className="card-body">
                {/* Editable Content */}
                <input
                    type="text"
                    value={content}  // Use state value for content
                    onChange={handleContentChange}  // Update state when content changes
                    className="form-control"
                />
                {/* Editable Priority */}
                <input
                    type="number"
                    value={priority}  // Use state value for priority
                    onChange={handlePriorityChange}  // Update state when priority changes
                    className="form-control"
                    min="1"
                    max="5"
                />
                <button onClick={() => removeTask(id)}>x</button>
                <button onClick={() => updateStatus(id, (item.status || 0) + 1)}>+</button>
                <button onClick={() => updateStatus(id, (item.status || 0) - 1)}>-</button>
                <button onClick={() => showTasks()}>o</button>
            </div>
        </div>
    )
}

export default Task;