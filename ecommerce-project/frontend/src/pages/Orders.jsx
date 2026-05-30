import { useEffect, useState } from "react";
import API from "../services/api";

function Orders() {
  const [customers, setCustomers] = useState([]);
  const [products, setProducts] = useState([]);

  const [customerId, setCustomerId] = useState("");
  const [productId, setProductId] = useState("");
  const [quantity, setQuantity] = useState("");

  const [orders, setOrders] = useState([]);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    const c = await API.get("/customers");
    const p = await API.get("/products");
    const o = await API.get("/orders");

    setCustomers(c.data);
    setProducts(p.data);
    setOrders(o.data);
  };

  const createOrder = async () => {
    try {
      await API.post("/orders", {
        customer_id: Number(customerId),
        product_id: Number(productId),
        quantity: Number(quantity),
      });

      loadData();
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Orders</h1>

      <h2>Create Order</h2>

      <select onChange={(e) => setCustomerId(e.target.value)}>
        <option>Select Customer</option>
        {customers.map((c) => (
          <option key={c.id} value={c.id}>
            {c.name}
          </option>
        ))}
      </select>

      <br />

      <select onChange={(e) => setProductId(e.target.value)}>
        <option>Select Product</option>
        {products.map((p) => (
          <option key={p.id} value={p.id}>
            {p.name}
          </option>
        ))}
      </select>

      <br />

      <input
        placeholder="Quantity"
        value={quantity}
        onChange={(e) => setQuantity(e.target.value)}
      />

      <br />

      <button onClick={createOrder}>Place Order</button>

      <h2>All Orders</h2>

      {orders.map((o) => (
        <div key={o.id} style={{ border: "1px solid black", margin: 10, padding: 10 }}>
            <p>Customer: {o.customer_name}</p>
            <p>Product: {o.product_name}</p>
            <p>Quantity: {o.quantity}</p>
        </div>
      ))}
    </div>
  );
}

export default Orders;