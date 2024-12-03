import React, { useState, useEffect, useRef } from "react";
import Status from "./Status.jsx"
import { useTask } from './TaskContext.jsx'

const Board = () => {

    const { tasks } = useTask();
    const [backLogItems, setBacklogItems] = useState([]);
    const [todoItems, setTodoItems] = useState([]);
    const [inProgressItems, setInProgressItems] = useState([]);
    const [reviewItems, setReviewItems] = useState([]);
    const [doneItems, setDoneItems] = useState([]);

    const countRef = useRef(0);
    const [count, setCount] = useState(0);  

    useEffect(() => {
        countRef.current = countRef.current + 1;
        console.log("XXX")
    });

    useEffect(() => {
        console.log("###")
    }, []);

    useEffect(() => {
        if (tasks.length >= 0) {
            setBacklogItems(tasks.filter(d => d.status === null || d.status === 0 ));
            setTodoItems(tasks.filter(d => d.status === 1));
            setInProgressItems(tasks.filter(d => d.status === 2));
            setReviewItems(tasks.filter(d => d.status === 3));
            setDoneItems(tasks.filter(d => d.status === 4));
        }
    }, [tasks]);

    useEffect(() => {
        // console.log("### Count Changes: " + count);
    }, [count]);

    const increaseOne = () => {
        setCount(count + 1);
    };

    const decreaseOne = () => {
        setCount(count - 1);
    };

    const reset = () => {
        setCount(0);
    };

    const submit = () => {
        console.log(backLogItems);
    }

    return (
        <div className="container mt-4">
            <div>{countRef.current}</div>
            <div className="row">
                <Status status={"To do"} items={todoItems} />
                <Status status={"In progress"} items={inProgressItems} />
                <Status status={"Review"} items={reviewItems} />
                <Status status={"Done"} items={doneItems} />
                <Status status={"Backlog"} items={backLogItems} />
            </div>
            <button onClick={submit}>Submit</button>
            <h1>{count}</h1>
            <button onClick={increaseOne}>Increase</button>
            <button onClick={decreaseOne}>Decrease</button>
            <button onClick={reset}>Reset</button>
        </div>
    )
}

export default Board;