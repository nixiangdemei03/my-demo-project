import { useEffect, useState } from "react";

export default function App() {
  const [msg, setMsg] = useState("loading...");

  useEffect(() => {
    fetch("/api/hello")
      .then((res) => res.json())
      .then((data) => setMsg(data.msg))
      .catch(() => setMsg("error"));
  }, []);

  return <h1>{msg}</h1>;
}
