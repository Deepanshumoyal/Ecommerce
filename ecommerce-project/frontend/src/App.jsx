import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Products from "./pages/Products";
import Customers from "./pages/Customers";
import Orders from "./pages/Orders";

function App() {
  return (
    <BrowserRouter>
      <div style={{ fontFamily: "Arial" }}>

        {/* NAVBAR */}
        <div style={{
          display: "flex",
          gap: "20px",
          padding: "15px",
          background: "#111",
          color: "white"
        }}>
          <Link style={{ color: "white" }} to="/">Products</Link>
          <Link style={{ color: "white" }} to="/customers">Customers</Link>
          <Link style={{ color: "white" }} to="/orders">Orders</Link>
        </div>

        {/* ROUTES */}
        <Routes>
          <Route path="/" element={<Products />} />
          <Route path="/customers" element={<Customers />} />
          <Route path="/orders" element={<Orders />} />
        </Routes>

      </div>
    </BrowserRouter>
  );
}

export default App;