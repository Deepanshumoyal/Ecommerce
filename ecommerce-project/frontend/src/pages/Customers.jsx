import { useEffect, useState } from "react";
import API from "../services/api";

function Customers() {
  const [customers, setCustomers] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    loadCustomers();
  }, []);

  const loadCustomers = async () => {
    const res = await API.get("/customers");
    setCustomers(res.data);
  };

  const createCustomer = async () => {
    await API.post("/customers", {
      name,
      email,
    });

    loadCustomers();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Customers</h1>

      <input placeholder="Name" onChange={(e) => setName(e.target.value)} />
      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />

      <button onClick={createCustomer}>Add Customer</button>

      {customers.map((c) => (
        <div key={c.id}>
          <h3>{c.name}</h3>
          <p>{c.email}</p>
        </div>
      ))}
    </div>
  );
}

export default Customers;