import React, { memo, useState, useEffect, useCallback } from "react";

const Todos = ({ todos, addTodo }) => {

    useEffect(() => { 
        console.log("child render");
    });

    return (
        <>
            <h2>My Todos</h2>
            {todos.map((todo, index) => {
                return <p key={index}>{todo}</p>;
            })}
            <button onClick={addTodo}>Add Todo</button>
        </>
    );
};

const MemoComponent = memo(Todos);

const ParentComponent = () => {
    const [count, setCount] = useState(0);
    const [todos, setTodos] = useState([]);

    const increment = () => {
        setCount((c) => c + 1);
    };

    const addTodo = () => {
        setTodos((t) => [...t, "New Todo"]);
    };

    // const addTodo = useCallback(() => {
    //     setTodos((t) => [...t, "New Todo"]);
    // }, [todos]);

    return (
        <>
            <MemoComponent todos={todos} addTodo={addTodo} />
            <hr />
            <div>
                Count: {count}
                <button onClick={increment}>+</button>
            </div>
        </>
    );
};

export default ParentComponent;

