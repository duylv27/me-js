import TaskProvider from "../components/TaskContext.jsx";
import Board from "../components/Kanban.jsx";

const Dashboard = () => {
    return (
        <TaskProvider>
            <Board/>
        </TaskProvider>
    );
}

export default Dashboard;