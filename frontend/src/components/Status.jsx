import Task from './Task';

const Status = ({ status, items }) => {

    return (
        <div className="col-12 col-md-3 mb-3">
            <h3>{status}</h3>
            <div className="kanban-column" style={{ minHeight: '200px', border: '1px solid #ddd', padding: '10px' }}>
                {items.map((task) => (
                    <div className="col-3 col-md-12 mb-3" key={task.id}>
                        <Task item={task} />
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Status;