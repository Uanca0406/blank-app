import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import React, {useState} from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function EstimasiKetidakpastian() {
  const [values, setValues] = useState([""]);
  const [result, setResult] = useState(null);

  const handleChange = (index, value) => {
    const newValues = [...values];
    newValues[index] = value;
    setValues(newValues);
  };

  const addField = () => setValues([...values, ""]);

  const calculateUncertainty = () => {
    const nums = values.map((v) => parseFloat(v)).filter((v) => !isNaN(v));
    const n = nums.length;
    if (n === 0) return;

    const mean = nums.reduce((a, b) => a + b, 0) / n;
    const stdDev = Math.sqrt(
      nums.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / (n - 1)
    );
    const uncertainty = stdDev / Math.sqrt(n);

    setResult({ mean, stdDev, uncertainty });
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Estimasi Ketidakpastian</h1>
      <Card>
        <CardContent className="space-y-2 p-4">
          {values.map((val, idx) => (
            <Input
              key={idx}
              type="number"
              value={val}
              onChange={(e) => handleChange(idx, e.target.value)}
              placeholder={`Nilai ${idx + 1}`}
            />
          ))}
          <div className="flex space-x-2">
            <Button onClick={addField}>Tambah Nilai</Button>
            <Button onClick={calculateUncertainty}>Hitung</Button>
          </div>
          {result && (
            <div className="mt-4">
              <p>Rata-rata: {result.mean.toFixed(4)}</p>
              <p>Simpangan Baku: {result.stdDev.toFixed(4)}</p>
              <p>Ketidakpastian: {result.uncertainty.toFixed(4)}</p>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
