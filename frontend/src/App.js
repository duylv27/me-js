import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from '@pages/Dashboard.jsx';
import ParentComponent from './components/ExpensiveStuff';

import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard/>} />
        <Route path="/useCallback" element={<ParentComponent/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
