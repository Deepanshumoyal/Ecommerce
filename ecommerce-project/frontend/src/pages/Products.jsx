import { useEffect, useState } from "react";
import API from "../services/api";

function Products() {
  const [products, setProducts] = useState([]);
  const [name, setName] = useState("");
  const [sku, setSku] = useState("");
  const [price, setPrice] = useState("");
  const [stock, setStock] = useState("");

  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async () => {
    try {
      const res = await API.get("/products");
      setProducts(res.data);
    } catch (err) {
      console.log(err);
    }
  };
 const createProduct = async () => {
  try {
    if (!name || !sku || !price || !stock) {
      alert("All fields are required");
      return;
    }

    const payload = {
      name: name.trim(),
      sku: sku.trim(),
      price: Number(price),
      stock: Number(stock),
    };

    console.log("PAYLOAD SENT:", payload);

    const res = await API.post("/products", payload);

    console.log("SUCCESS RESPONSE:", res.data);

    loadProducts();

    setName("");
    setSku("");
    setPrice("");
    setStock("");

  } catch (err) {
    console.log("ERROR:", err.response?.data || err.message);
  }
};
  return (
    <div style={{ padding: "20px" }}>
      <h1>Products</h1>
      <h2>Create Product</h2>

<div style={{ marginBottom: "20px" }}>
  <input
    placeholder="Name"
    value={name}
    onChange={(e) => setName(e.target.value)}
  />
  <br />

  <input
    placeholder="SKU"
    value={sku}
    onChange={(e) => setSku(e.target.value)}
  />
  <br />

  <input
    placeholder="Price"
    value={price}
    onChange={(e) => setPrice(e.target.value)}
  />
  <br />

  <input
    placeholder="Stock"
    value={stock}
    onChange={(e) => setStock(e.target.value)}
  />
  <br />

  <button onClick={createProduct}>
    Add Product
  </button>
 
</div>

      {products.map((p) => (
  <div
    key={p.id}
    style={{
      border: "1px solid #ddd",
      margin: "10px 0",
      padding: "15px",
      borderRadius: "8px",
      background: "#f9f9f9"
    }}
  >
    <h3 style={{ marginBottom: "5px" }}>{p.name}</h3>

    <p><b>SKU:</b> {p.sku}</p>
    <p><b>Price:</b> ₹{p.price}</p>

    <p style={{ color: p.stock < 5 ? "red" : "green" }}>
      <b>Stock:</b> {p.stock}
    </p>
    <button
      onClick={async () => {
        await API.delete(`/products/${p.id}`);
        loadProducts();
         }}
      style={{
        background: "red",
        color: "white",
        border: "none",
        padding: "6px 10px",
        borderRadius: "5px",
        cursor: "pointer"
      }}
    >   
       Delete
     </button>
   </div>
      ))}
    </div>
  );
}

export default Products;